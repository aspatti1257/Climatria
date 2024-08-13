import { AppBar, Box, Toolbar, Typography } from "@mui/material";
import climatriaLogo from "../assets/climatriaLogo.svg";

const Header = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{ backgroundColor: "#045652" }}>
        <Toolbar sx={{ justifyContent: "center" }}>
          <Box
            component="img"
            src={climatriaLogo}
            alt="Climatria Logo"
            sx={{ height: 40, marginRight: 1 }}
          />
          <Typography
            variant="h6"
            component="div"
            sx={{
              color: "#fff",
              mt: "8px",
              fontFamily: "'Poppins', sans-serif",
              fontWeight: 400,
              fontSize: "30px",
              lineHeight: "120%",
            }}
          >
            Climatria
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default Header;
