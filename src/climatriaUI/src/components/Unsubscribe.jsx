import { useState } from "react";
import validate from "validate.js";
import {
  Box,
  Container,
  Grid,
  Button,
  TextField,
  Typography,
} from "@mui/material";

const Unsubscribe = () => {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [formErrors, setFormErrors] = useState({});
  const VITE_BASE_URL = import.meta.env.VITE_BASE_URL;

  // Validation schema
  const schema = {
    email: {
      presence: { allowEmpty: false, message: "is required" },
      email: { message: "is not valid" },
    },
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
    setFormErrors({});
  };

  const handleUnsubscribe = async () => {
    // Validate the form data
    const errors = validate({ email }, schema);
    setFormErrors(errors || {});

    if (!errors) {
      try {
        const response = await fetch(`${VITE_BASE_URL}/api/unsubscribe`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email }),
        });

        if (response.ok) {
          setMessage("You have successfully unsubscribed.");
        } else if (response.status === 404) {
          setMessage("Email not found. Please check and try again.");
        } else {
          setMessage("Failed to unsubscribe. Please try again.");
        }
      } catch (error) {
        console.error("Error:", error);
        setMessage("An error occurred. Please try again later.");
      }
    }
  };

  return (
    <Box
      sx={{
        width: "100%",
        backgroundColor: "#FFFFFF",
        padding: "2rem 0",
        borderRadius: "8px",
      }}
    >
      <Container maxWidth="sm">
        <Typography
          variant="h4"
          align="center"
          gutterBottom
          color="textSecondary"
        >
          Unsubscribe from Alerts
        </Typography>
        <Box
          sx={{
            backgroundColor: "#FFFFFF",
            padding: "2rem",
            borderRadius: "8px",
          }}
        >
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField
                label="Email"
                variant="outlined"
                fullWidth
                sx={{ marginBottom: "1rem" }}
                value={email}
                onChange={handleEmailChange}
                error={!!formErrors.email}
                helperText={formErrors.email ? formErrors.email[0] : ""}
              />
            </Grid>
            <Grid item xs={12}>
              <Button
                variant="contained"
                color="primary"
                fullWidth
                onClick={handleUnsubscribe}
              >
                Unsubscribe
              </Button>
            </Grid>
          </Grid>
          {message && (
            <Typography
              variant="body2"
              sx={{
                marginTop: "1.5rem",
                color: "#4CAF50",
                fontFamily: "'Poppins', sans-serif",
                fontSize: "16px",
                textAlign: "center",
              }}
            >
              {message}
            </Typography>
          )}
        </Box>
      </Container>
    </Box>
  );
};

export default Unsubscribe;
