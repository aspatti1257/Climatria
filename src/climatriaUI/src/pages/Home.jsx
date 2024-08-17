import { useState, useEffect, useRef } from "react";
import PropTypes from "prop-types";
import { Box, Typography, Container, Grid } from "@mui/material";
import FormSection from "../components/FormSection";
import Unsubscribe from "../components/Unsubscribe";
import NotificationsNoneIcon from "@mui/icons-material/NotificationsNone";
import HealthAndSafetyOutlinedIcon from "@mui/icons-material/HealthAndSafetyOutlined";
import MenuBookOutlinedIcon from "@mui/icons-material/MenuBookOutlined";

import treeImage from "../assets/treeImage.svg";

function Home({ isUnsubscribing, VITE_BASE_URL }) {
  const [balancingAuthorities, setBalancingAuthorities] = useState([]);
  const formSectionRef = useRef(null);

  useEffect(() => {
    const fetchBalancingAuthorities = async () => {
      try {
        const response = await fetch(
          `${VITE_BASE_URL}/api/balancing_authorities`
        );
        if (response.ok) {
          const data = await response.json();
          setBalancingAuthorities(data);
        } else {
          console.error("Failed to fetch balancing authorities");
        }
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchBalancingAuthorities();
  }, []);

  useEffect(() => {
    if (isUnsubscribing && formSectionRef.current) {
      formSectionRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [isUnsubscribing]);

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
        ref={formSectionRef} // Add the ref here
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

          {isUnsubscribing ? (
            <Unsubscribe />
          ) : (
            <FormSection
              balancingAuthorities={balancingAuthorities}
              VITE_BASE_URL={VITE_BASE_URL}
            />
          )}
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

Home.propTypes = {
  isUnsubscribing: PropTypes.bool.isRequired,
  setIsUnsubscribing: PropTypes.func.isRequired,
  VITE_BASE_URL: PropTypes.string.isRequired,
};

export default Home;
