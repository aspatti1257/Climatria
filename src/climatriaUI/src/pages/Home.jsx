import { useState } from "react";
import {
  Box,
  Typography,
  Container,
  Grid,
  Button,
  TextField,
  Checkbox,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  FormControlLabel,
} from "@mui/material";
import ElectricalServicesOutlinedIcon from "@mui/icons-material/ElectricalServicesOutlined";
import NotificationsNoneIcon from "@mui/icons-material/NotificationsNone";
import HealthAndSafetyOutlinedIcon from "@mui/icons-material/HealthAndSafetyOutlined";
import MenuBookOutlinedIcon from "@mui/icons-material/MenuBookOutlined";
import WaterDropOutlinedIcon from "@mui/icons-material/WaterDropOutlined";
import ForestOutlinedIcon from "@mui/icons-material/ForestOutlined";
import treeImage from "../assets/treeImage.svg";
// import waveBorder from "../assets/waveBorder.svg";

function Home() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phoneNumber: "",
    zipCode: "",
    balancingAuthority: "",
    frequency: "daily",
    notifications: {
      energy: false,
      water: false,
      airQuality: false,
    },
  });

  const API_BASE_URL = "http://3.145.3.230:8080";

  const [showVerification, setShowVerification] = useState(false);

  const [verificationData, setVerificationData] = useState({
    verificationId: "",
    code: "",
  })

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleVerifyChange = (event) => {
    const { name, value } = event.target;
      setVerificationData((prevData) => ({
        ...prevData,
        [name]: value
    }));
  }

  const handleCheckboxChange = (event) => {
    const { name, checked } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      notifications: {
        ...prevData.notifications,
        [name]: checked,
      },
    }));
  };

  const handleStartVerify = async () => {
    try {
      const startVerificationResponse = await fetch(`${API_BASE_URL}/api/start_verification`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      if (startVerificationResponse.ok) {
          const data = await startVerificationResponse.json();
          console.log(data.verificationId);
          setVerificationData({
              verificationId: data.verificationId,
              code: "YOUR CODE HERE"
          });
          setShowVerification(true);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const handleCodeSubmit = async () => {
    try {
      const reportCodeResponse = await fetch(`${API_BASE_URL}/api/report_code`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(verificationData),
      });
      if (reportCodeResponse.ok) {
        const data = await reportCodeResponse.json();
        if (data) {
            await handleFormSubmit();
        }
      }
    } catch (error) {
      console.error("Error:", error)
    }
  };

  const handleFormSubmit = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/signup`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        console.log("User signed up successfully");
        setShowVerification(false);
      } else {
        console.error("Failed to sign up user");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <>
      <Box
        sx={{ width: "100%", backgroundColor: "#045652", padding: "2rem 0" }}
      >
        {/* Hero Section */}
        <Container maxWidth="lg">
          <Box sx={{ textAlign: "center", marginBottom: "2rem" }}>
            <Typography
              variant="h3"
              component="h1"
              sx={{
                color: "#FFFFFF",
                fontWeight: 600,
                fontSize: "48px",
                lineHeight: "120%",
                marginBottom: "1rem",
                fontFamily: "'Poppins', sans-serif",
              }}
            >
              Support climate issues in your area when it needs YOU the most.
            </Typography>
            <Typography
              variant="subtitle1"
              component="p"
              sx={{
                color: "#FFFFFF",
                fontWeight: 400,
                fontSize: "17px",
                lineHeight: "140%",
                marginBottom: "16px",
                fontFamily: "'Poppins', sans-serif",
              }}
            >
              Real Time Alerting, with an Impact.
            </Typography>
            <Box
              component="img"
              src={treeImage}
              alt="Hero Graphic"
              sx={{
                width: "100%",
                maxWidth: "200px",
                margin: "0 auto",
                bottom: "10px",
              }}
            />
          </Box>
        </Container>
      </Box>
      <Box
        sx={{
          width: "100%",
          backgroundColor: "#9F5B4B",
          padding: "4rem 0",
          color: "#FFFFFF",
          textAlign: "center",
        }}
      >
        <Container maxWidth="md">
          <Typography
            variant="h4"
            component="h2"
            sx={{
              fontWeight: 600,
              marginBottom: "2rem",
              fontFamily: "'Poppins', sans-serif",
            }}
          >
            How it works
          </Typography>

          <Typography
            variant="body1"
            component="p"
            sx={{
              fontSize: "18px",
              marginBottom: "1rem",
              fontFamily: "'Poppins', sans-serif",
            }}
          >
            1. Sign up in seconds by selecting the alerts you want to receive
            and providing us with a few key details.
          </Typography>

          <Typography
            variant="body1"
            component="p"
            sx={{
              fontSize: "18px",
              marginBottom: "1rem",
              fontFamily: "'Poppins', sans-serif",
            }}
          >
            2. Let our Dynamic Prediction Model send you real-time alerts when
            your area is having issues.
          </Typography>

          <Typography
            variant="body1"
            component="p"
            sx={{
              fontSize: "18px",
              marginBottom: "3rem",
              fontFamily: "'Poppins', sans-serif",
            }}
          >
            3. Take tangible steps to support climate issues impacting your
            community immediately.
          </Typography>

          {/* Form Section */}
          <Box
            sx={{
              backgroundColor: "#FFFFFF",
              padding: "2rem",
              borderRadius: "8px",
              color: "#000000",
              textAlign: "left",
            }}
          >
            {showVerification ?
              <Grid container spacing={2}>
                <TextField
                  label="Code"
                  variant="outlined"
                  fullWidth
                  sx={{marginBottom: "1rem"}}
                  name="code"
                  value={verificationData.code}
                  onChange={handleVerifyChange}
                />
              <Button
                  variant="contained"
                  color="primary"
                  fullWidth
                  onClick={handleCodeSubmit}
              >
                  Verify
              </Button>
              </Grid> :
              <Grid container spacing={2}>
                <Grid item xs={12} md={6}>
                <FormControlLabel
                  control={
                    <Checkbox
                      checked={formData.notifications.energy}
                      onChange={handleCheckboxChange}
                      name="energy"
                    />
                  }
                  label={
                    <Box
                      sx={{
                        fontSize: "16px",
                        fontFamily: "'Poppins', sans-serif",
                      }}
                    >
                      <strong>“Dirty” Energy on the Grid</strong>
                      <ElectricalServicesOutlinedIcon
                        sx={{ marginRight: "0.5rem" }}
                      />{" "}
                      <Typography
                        variant="body2"
                        sx={{ fontSize: "14px", color: "#555555" }}
                      >
                        During high usage periods the electric grid uses peaker
                        plants (typically coal) to support the electricity
                        demand.
                      </Typography>
                    </Box>
                  }
                />
                <FormControlLabel
                  control={
                    <Checkbox
                      checked={formData.notifications.water}
                      onChange={handleCheckboxChange}
                      name="water"
                    />
                  }
                  label={
                    <Box
                      sx={{
                        fontSize: "16px",
                        fontFamily: "'Poppins', sans-serif",
                      }}
                    >
                      <strong>Water Quality is Low</strong>
                      <WaterDropOutlinedIcon
                        sx={{ marginRight: "0.5rem" }}
                      />{" "}
                      <Typography
                        variant="body2"
                        sx={{ fontSize: "14px", color: "#555555" }}
                      >
                        When pollution or algae hit the waterways, your water
                        quality can be affected.
                      </Typography>
                    </Box>
                  }
                />
                <FormControlLabel
                  control={
                    <Checkbox
                      checked={formData.notifications.airQuality}
                      onChange={handleCheckboxChange}
                      name="airQuality"
                    />
                  }
                  label={
                    <Box
                      sx={{
                        fontSize: "16px",
                        fontFamily: "'Poppins', sans-serif",
                      }}
                    >
                      <strong>Air Quality is Low</strong>
                      <ForestOutlinedIcon sx={{ marginRight: "0.5rem" }} />{" "}
                      <Typography
                        variant="body2"
                        sx={{ fontSize: "14px", color: "#555555" }}
                      >
                        Forest fires and pollution can contribute to poor air
                        quality.
                      </Typography>
                    </Box>
                  }
                />
              </Grid>
                <Grid item xs={12} md={6}>
                <TextField
                  label="Name"
                  variant="outlined"
                  fullWidth
                  sx={{ marginBottom: "1rem" }}
                  name="name"
                  value={formData.name}
                  onChange={handleInputChange}
                />
                <TextField
                  label="Email"
                  variant="outlined"
                  fullWidth
                  sx={{ marginBottom: "1rem" }}
                  name="email"
                  value={formData.email}
                  onChange={handleInputChange}
                />
                <TextField
                  label="Phone Number"
                  variant="outlined"
                  fullWidth
                  sx={{ marginBottom: "1rem" }}
                  name="phoneNumber"
                  value={formData.phoneNumber}
                  onChange={handleInputChange}
                />
                <TextField
                  label="Zip Code"
                  variant="outlined"
                  fullWidth
                  sx={{ marginBottom: "1rem" }}
                  name="zipCode"
                  value={formData.zipCode}
                  onChange={handleInputChange}
                />
                <TextField
                  label="Balancing Authority"
                  variant="outlined"
                  fullWidth
                  sx={{ marginBottom: "1rem" }}
                  name="balancingAuthority"
                  value={formData.balancingAuthority}
                  onChange={handleInputChange}
                />
                <FormControl fullWidth sx={{ marginBottom: "1rem" }}>
                  <InputLabel>Frequency</InputLabel>
                  <Select
                    label="Frequency"
                    name="frequency"
                    value={formData.frequency}
                    onChange={handleInputChange}
                  >
                    <MenuItem value="daily">Daily</MenuItem>
                    <MenuItem value="weekly">Weekly</MenuItem>
                  </Select>
                </FormControl>
                <Button
                  variant="contained"
                  color="primary"
                  fullWidth
                  onClick={handleStartVerify}
                >
                  Sign Up
                </Button>
              </Grid>
              </Grid>
            }
          </Box>
        </Container>
      </Box>
      <Box
        sx={{
          width: "100%",
          backgroundColor: "#004e48",
          padding: "4rem 0",
          textAlign: "center",
          color: "#FFFFFF",
        }}
      >
        <Container maxWidth="lg">
          <Typography
            variant="h4"
            component="h2"
            sx={{
              fontWeight: 600,
              marginBottom: "3rem",
              fontFamily: "'Poppins', sans-serif",
            }}
          >
            Why Climatria?
          </Typography>
          <Grid container spacing={4}>
            <Grid item xs={12} md={4}>
              <Box
                sx={{
                  backgroundColor: "#9A6B5A",
                  padding: "2rem",
                  borderRadius: "8px",
                  textAlign: "center",
                }}
              >
                <NotificationsNoneIcon
                  sx={{
                    fontSize: "80px",
                    marginBottom: "1rem",
                    color: "#FFFFFF",
                  }}
                />
                <Typography
                  variant="h6"
                  component="h3"
                  sx={{
                    fontWeight: 600,
                    marginBottom: "0.5rem",
                    fontFamily: "'Poppins', sans-serif",
                  }}
                >
                  Get real-time alerts
                </Typography>
                <Typography
                  variant="body2"
                  component="p"
                  sx={{
                    fontSize: "16px",
                    fontFamily: "'Poppins', sans-serif",
                    color: "#FFFFFF",
                  }}
                >
                  Get alerts in real time to issues affecting your area so
                  you’re “in the know”.
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} md={4}>
              <Box
                sx={{
                  backgroundColor: "#9A6B5A",
                  padding: "2rem",
                  borderRadius: "8px",
                  textAlign: "center",
                }}
              >
                <HealthAndSafetyOutlinedIcon
                  sx={{
                    fontSize: "80px",
                    marginBottom: "1rem",
                    color: "#FFFFFF",
                  }}
                />
                <Typography
                  variant="h6"
                  component="h3"
                  sx={{
                    fontWeight: 600,
                    marginBottom: "0.5rem",
                    fontFamily: "'Poppins', sans-serif",
                  }}
                >
                  Make a direct impact
                </Typography>
                <Typography
                  variant="body2"
                  component="p"
                  sx={{
                    fontSize: "16px",
                    fontFamily: "'Poppins', sans-serif",
                    color: "#FFFFFF",
                  }}
                >
                  Find simple ways to positively contribute to real issues in
                  your own backyard.
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} md={4}>
              <Box
                sx={{
                  backgroundColor: "#9A6B5A",
                  padding: "2rem",
                  borderRadius: "8px",
                  textAlign: "center",
                }}
              >
                <MenuBookOutlinedIcon
                  sx={{
                    fontSize: "80px",
                    marginBottom: "1rem",
                    color: "#FFFFFF",
                  }}
                />
                <Typography
                  variant="h6"
                  component="h3"
                  sx={{
                    fontWeight: 600,
                    marginBottom: "0.5rem",
                    fontFamily: "'Poppins', sans-serif",
                  }}
                >
                  Learn about issues
                </Typography>
                <Typography
                  variant="body2"
                  component="p"
                  sx={{
                    fontSize: "16px",
                    fontFamily: "'Poppins', sans-serif",
                    color: "#FFFFFF",
                  }}
                >
                  Dive into the issues in your area so that you can be more
                  knowledgeable.
                </Typography>
              </Box>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </>
  );
}

export default Home;
