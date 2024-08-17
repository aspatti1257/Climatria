import { useState, useMemo } from "react";
import PropTypes from "prop-types";
import validate from "validate.js";
import {
  Grid,
  TextField,
  Checkbox,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  FormControlLabel,
  Autocomplete,
  Button,
  Box,
  Typography,
} from "@mui/material";
import WaterDropOutlinedIcon from "@mui/icons-material/WaterDropOutlined";
import ForestOutlinedIcon from "@mui/icons-material/ForestOutlined";
import ElectricalServicesOutlinedIcon from "@mui/icons-material/ElectricalServicesOutlined";

const FormSection = ({ balancingAuthorities, VITE_BASE_URL }) => {
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

  const [formErrors, setFormErrors] = useState({});

  const schema = useMemo(
    () => ({
      name: {
        presence: { allowEmpty: false, message: "is required" },
        length: { maximum: 128 },
      },
      email: {
        presence: { allowEmpty: false, message: "is required" },
        email: { message: "is not valid" },
        length: { maximum: 300 },
      },
      phoneNumber: {
        presence: { allowEmpty: false, message: "is required" },
        format: {
          pattern: /^\+?\d{11,12}$/,
          message:
            "must be a valid phone number with country code (11-12 digits)",
        },
      },
      zipCode: {
        presence: { allowEmpty: false, message: "is required" },
        format: {
          pattern: /^\d{5}(-\d{4})?$/,
          message: "must be a valid zip code",
        },
      },
      balancingAuthority: {
        presence: { allowEmpty: false, message: "is required" },
      },
    }),
    []
  );

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleAutocompleteChange = (event, newValue) => {
    setFormData((prevData) => ({
      ...prevData,
      balancingAuthority: newValue || "",
    }));
  };

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

  const handleSubmit = async () => {
    const errors = validate(formData, schema);
    setFormErrors(errors || {});

    if (!errors) {
      try {
        const response = await fetch(`${VITE_BASE_URL}/api/signup`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        });

        if (response.ok) {
          console.log("User signed up successfully");
        } else {
          console.error("Failed to sign up user");
        }
      } catch (error) {
        console.error("Error:", error);
      }
    }
  };

  const hasError = (field) => !!formErrors[field];

  return (
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
                  During high usage periods the electric grid uses peaker plants
                  (typically coal) to support the electricity demand.
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
                <WaterDropOutlinedIcon sx={{ marginRight: "0.5rem" }} />{" "}
                <Typography
                  variant="body2"
                  sx={{ fontSize: "14px", color: "#555555" }}
                >
                  When pollution or algae hit the waterways, your water quality
                  can be affected.
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
                  Forest fires and pollution can contribute to poor air quality.
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
            error={hasError("name")}
            helperText={formErrors.name ? formErrors.name[0] : null}
          />
          <TextField
            label="Email"
            variant="outlined"
            fullWidth
            sx={{ marginBottom: "1rem" }}
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            error={hasError("email")}
            helperText={formErrors.email ? formErrors.email[0] : null}
          />
          <TextField
            label="Phone Number"
            variant="outlined"
            fullWidth
            sx={{ marginBottom: "1rem" }}
            name="phoneNumber"
            value={formData.phoneNumber}
            onChange={handleInputChange}
            error={hasError("phoneNumber")}
            helperText={
              formErrors.phoneNumber
                ? formErrors.phoneNumber[0]
                : "Include country code (e.g., +1)"
            }
          />
          <TextField
            label="Zip Code"
            variant="outlined"
            fullWidth
            sx={{ marginBottom: "1rem" }}
            name="zipCode"
            value={formData.zipCode}
            onChange={handleInputChange}
            error={hasError("zipCode")}
            helperText={formErrors.zipCode ? formErrors.zipCode[0] : null}
          />
          <Autocomplete
            options={balancingAuthorities}
            getOptionLabel={(option) => option}
            fullWidth
            sx={{ marginBottom: "1rem" }}
            renderInput={(params) => (
              <TextField
                {...params}
                label="Balancing Authority"
                variant="outlined"
                name="balancingAuthority"
                error={hasError("balancingAuthority")}
                helperText={
                  formErrors.balancingAuthority
                    ? formErrors.balancingAuthority[0]
                    : null
                }
              />
            )}
            onChange={handleAutocompleteChange}
            value={formData.balancingAuthority}
            isOptionEqualToValue={(option, value) =>
              option === value || value === ""
            }
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
            onClick={handleSubmit}
          >
            Sign Up
          </Button>
        </Grid>
      </Grid>
    </Box>
  );
};

FormSection.propTypes = {
  balancingAuthorities: PropTypes.arrayOf(PropTypes.string).isRequired,
  VITE_BASE_URL: PropTypes.string.isRequired,
};

export default FormSection;
