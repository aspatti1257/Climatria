import {
  Box,
  Typography,
  Container,
  Grid,
  Button,
  TextField,
  Checkbox,
  FormControlLabel,
} from "@mui/material";
import ElectricBoltOutlinedIcon from "@mui/icons-material/ElectricBoltOutlined";
import treeImage from "../assets/treeImage.svg";
// import waveBorder from "../assets/waveBorder.svg";

function Home() {
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
            <Grid container spacing={2}>
              <Grid item xs={12} md={6}>
                <FormControlLabel
                  control={<Checkbox defaultChecked />}
                  label={
                    <Box
                      sx={{
                        fontSize: "16px",
                        fontFamily: "'Poppins', sans-serif",
                      }}
                    >
                      <strong>“Dirty” Energy on the Grid</strong>
                      <ElectricBoltOutlinedIcon
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
                  control={<Checkbox />}
                  label={
                    <Box
                      sx={{
                        fontSize: "16px",
                        fontFamily: "'Poppins', sans-serif",
                      }}
                    >
                      <strong>Water Quality is Low 💧</strong>
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
                  control={<Checkbox />}
                  label={
                    <Box
                      sx={{
                        fontSize: "16px",
                        fontFamily: "'Poppins', sans-serif",
                      }}
                    >
                      <strong>Air Quality is Low 🌿</strong>
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
                />
                <TextField
                  label="Email"
                  variant="outlined"
                  fullWidth
                  sx={{ marginBottom: "1rem" }}
                />
                <TextField
                  label="Phone Number"
                  variant="outlined"
                  fullWidth
                  sx={{ marginBottom: "1rem" }}
                />
                <TextField
                  label="Zip Code"
                  variant="outlined"
                  fullWidth
                  sx={{ marginBottom: "1rem" }}
                />
                <TextField
                  label="Frequency"
                  variant="outlined"
                  fullWidth
                  sx={{ marginBottom: "1rem" }}
                />
                <Button variant="contained" color="primary" fullWidth>
                  Sign Up
                </Button>
              </Grid>
            </Grid>
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
                <Box
                  component="img"
                  // src={/* Insert path to bell icon */}
                  alt="Real-time alerts icon"
                  sx={{
                    width: "40px",
                    height: "40px",
                    marginBottom: "1rem",
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
                <Box
                  component="img"
                  // src={/* Insert path to handshake icon */}
                  alt="Direct impact icon"
                  sx={{
                    width: "40px",
                    height: "40px",
                    marginBottom: "1rem",
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
                <Box
                  component="img"
                  // src={/* Insert path to book icon */}
                  alt="Learn about issues icon"
                  sx={{
                    width: "40px",
                    height: "40px",
                    marginBottom: "1rem",
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
