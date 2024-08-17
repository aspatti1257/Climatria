import PropTypes from "prop-types";
import { Box, Typography, Link } from "@mui/material";

const Footer = ({ setIsUnsubscribing }) => {
  return (
    <Box
      sx={{
        width: "100%",
        backgroundColor: "#F8F8F8",
        padding: "1rem 0",
        textAlign: "center",
        borderTop: "1px solid #E0E0E0",
      }}
    >
      <Typography
        variant="body2"
        component="p"
        sx={{
          color: "#757575",
          fontFamily: "'Poppins', sans-serif",
          fontSize: "14px",
        }}
      >
        ©2024 Climatria •{" "}
        <Link href="#" sx={{ color: "#757575", textDecoration: "none" }}>
          Terms & Conditions
        </Link>{" "}
        •{" "}
        <Link href="#" sx={{ color: "#757575", textDecoration: "none" }}>
          Privacy
        </Link>{" "}
        •{" "}
        <Link
          href="#"
          sx={{ color: "#757575", textDecoration: "none" }}
          onClick={() => setIsUnsubscribing(true)}
        >
          Unsubscribe
        </Link>
      </Typography>
    </Box>
  );
};

Footer.propTypes = {
  setIsUnsubscribing: PropTypes.func.isRequired,
};

export default Footer;
