import { Box, Typography, Link } from "@mui/material";

function Footer() {
  return (
    <Box
      sx={{
        width: "100%",
        backgroundColor: "#F8F8F8", // Light background color
        padding: "1rem 0",
        textAlign: "center",
        borderTop: "1px solid #E0E0E0", // Optional: adds a top border for separation
      }}
    >
      <Typography
        variant="body2"
        component="p"
        sx={{
          color: "#757575", // Grey text color
          fontFamily: "'Poppins', sans-serif", // Use Poppins font
          fontSize: "14px", // Font size
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
        <Link href="#" sx={{ color: "#757575", textDecoration: "none" }}>
          Unsubscribe
        </Link>
      </Typography>
    </Box>
  );
}

export default Footer;
