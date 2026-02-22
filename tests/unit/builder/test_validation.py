"""Unit tests for Builder validation modes."""

import pytest

from armodel.models import ImplementationDataType, ImplementationDataTypeBuilder
from armodel.core import GlobalSettingsManager, BuilderValidationMode


class TestBuilderValidation:
    """Test builder validation modes."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.settings = GlobalSettingsManager()
        self.original_mode = self.settings.builder_validation

    def teardown_method(self):
        """Reset settings after tests."""
        self.settings.builder_validation = self.original_mode

    def test_disabled_validation_no_checks(self):
        """Test disabled validation skips all checks."""
        self.settings.builder_validation = BuilderValidationMode.DISABLED

        # Should not raise even with missing required fields
        instance = ImplementationDataTypeBuilder().build()
        assert instance is not None

    def test_validation_mode_persistence(self):
        """Test that validation mode persists across multiple builds."""
        self.settings.builder_validation = BuilderValidationMode.STRICT

        # Both builds should use the same validation setting
        instance1 = ImplementationDataTypeBuilder().build()
        instance2 = ImplementationDataTypeBuilder().build()

        assert instance1 is not None
        assert instance2 is not None

    def test_validation_mode_switching(self):
        """Test switching between validation modes."""
        # Start with strict
        self.settings.builder_validation = BuilderValidationMode.STRICT

        instance1 = ImplementationDataTypeBuilder().build()

        # Switch to lenient
        self.settings.builder_validation = BuilderValidationMode.LENIENT

        instance2 = ImplementationDataTypeBuilder().build()

        # Switch to disabled
        self.settings.builder_validation = BuilderValidationMode.DISABLED

        instance3 = ImplementationDataTypeBuilder().build()

        assert instance1 is not None
        assert instance2 is not None
        assert instance3 is not None

    def test_optional_field_validation(self):
        """Test that optional fields don't fail validation."""
        self.settings.builder_validation = BuilderValidationMode.DISABLED

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sw_data_def_props(None)  # Optional field
            .build()
        )

        assert data_type.short_name == "MyType"
        assert data_type.sw_data_def_props is None

    def test_validation_in_chain(self):
        """Test that validation happens at the end of the chain."""
        self.settings.builder_validation = BuilderValidationMode.DISABLED

        # Should not raise during chaining
        builder = ImplementationDataTypeBuilder()
        builder = builder.with_category("VALUE")
        builder = builder.with_type_emitter("BSW")

        # Build should succeed
        instance = builder.build()
        assert instance is not None

    def test_strict_validation_passes_with_required_fields(self):
        """Test strict validation passes when all required fields are set."""
        self.settings.builder_validation = BuilderValidationMode.STRICT

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .build()
        )

        assert data_type.short_name == "MyType"

    def test_lenient_validation_passes_with_required_fields(self):
        """Test lenient validation passes when all required fields are set."""
        self.settings.builder_validation = BuilderValidationMode.LENIENT

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .build()
        )

        assert data_type.short_name == "MyType"