import { Box, Container, Typography, Link } from "@mui/material";
import CelebrationIcon from "@mui/icons-material/Celebration";
import PropTypes from "prop-types";

const Welcome = ({ onUnsubscribe }) => {
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
        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            marginBottom: "1rem",
          }}
        >
          <CelebrationIcon
            sx={{
              fontSize: "3rem",
              color: "#FF6F61",
              marginRight: "0.5rem",
            }}
          />
          <Typography
            variant="h4"
            align="center"
            color="textSecondary"
            sx={{
              fontFamily: "'Poppins', sans-serif",
              fontWeight: 700,
            }}
          >
            Welcome to Climatria
          </Typography>
        </Box>
        <Box
          sx={{
            backgroundColor: "#FFFFFF",
            padding: "2rem",
            borderRadius: "8px",
            textAlign: "center",
          }}
        >
          <Typography
            variant="body1"
            sx={{
              fontFamily: "'Poppins', sans-serif",
              fontSize: "18px",
              marginBottom: "1rem",
              color: "#000000",
            }}
          >
            We&apos;re so excited to have you be a part of the Climatria family!
          </Typography>
          <Typography
            variant="body2"
            sx={{
              fontFamily: "'Poppins', sans-serif",
              fontSize: "16px",
              color: "#555555",
            }}
          >
            Note: you can always{" "}
            <Link
              href="#"
              sx={{ color: "#000000", textDecoration: "underline" }}
              onClick={onUnsubscribe}
            >
              unsubscribe
            </Link>{" "}
            at any time.
          </Typography>
        </Box>
      </Container>
    </Box>
  );
};

Welcome.propTypes = {
  onUnsubscribe: PropTypes.func.isRequired,
};

export default Welcome;
