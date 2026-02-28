"""DiagnosticEnvConditionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_condition_formula_part import (
    DiagnosticEnvConditionFormulaPart,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_condition_formula_part import DiagnosticEnvConditionFormulaPartBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition import (
    DiagnosticLogicalOperatorEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticEnvConditionFormula(DiagnosticEnvConditionFormulaPart):
    """AUTOSAR DiagnosticEnvConditionFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-ENV-CONDITION-FORMULA"


    nrc_value: Optional[PositiveInteger]
    op: Optional[DiagnosticLogicalOperatorEnum]
    _DESERIALIZE_DISPATCH = {
        "NRC-VALUE": lambda obj, elem: setattr(obj, "nrc_value", elem.text),
        "OP": lambda obj, elem: setattr(obj, "op", DiagnosticLogicalOperatorEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticEnvConditionFormula."""
        super().__init__()
        self.nrc_value: Optional[PositiveInteger] = None
        self.op: Optional[DiagnosticLogicalOperatorEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnvConditionFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnvConditionFormula, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nrc_value
        if self.nrc_value is not None:
            serialized = SerializationHelper.serialize_item(self.nrc_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NRC-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize op
        if self.op is not None:
            serialized = SerializationHelper.serialize_item(self.op, "DiagnosticLogicalOperatorEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvConditionFormula":
        """Deserialize XML element to DiagnosticEnvConditionFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvConditionFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnvConditionFormula, cls).deserialize(element)

        # Parse nrc_value
        child = SerializationHelper.find_child_element(element, "NRC-VALUE")
        if child is not None:
            nrc_value_value = child.text
            obj.nrc_value = nrc_value_value

        # Parse op
        child = SerializationHelper.find_child_element(element, "OP")
        if child is not None:
            op_value = DiagnosticLogicalOperatorEnum.deserialize(child)
            obj.op = op_value

        return obj



class DiagnosticEnvConditionFormulaBuilder(DiagnosticEnvConditionFormulaPartBuilder):
    """Builder for DiagnosticEnvConditionFormula with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEnvConditionFormula = DiagnosticEnvConditionFormula()


    def with_nrc_value(self, value: Optional[PositiveInteger]) -> "DiagnosticEnvConditionFormulaBuilder":
        """Set nrc_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nrc_value = value
        return self

    def with_op(self, value: Optional[DiagnosticLogicalOperatorEnum]) -> "DiagnosticEnvConditionFormulaBuilder":
        """Set op attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.op = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> DiagnosticEnvConditionFormula:
        """Build and return the DiagnosticEnvConditionFormula instance with validation."""
        self._validate_instance()
        pass
        return self._obj