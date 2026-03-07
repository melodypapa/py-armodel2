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
        "NRC-VALUE": lambda obj, elem: setattr(obj, "nrc_value", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "NRC-VALUE":
                setattr(obj, "nrc_value", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "OP":
                setattr(obj, "op", DiagnosticLogicalOperatorEnum.deserialize(child))

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
            raise ValueError("Attribute 'nrc_value' is required and cannot be None")
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
            raise ValueError("Attribute 'op' is required and cannot be None")
        self._obj.op = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "nrcValue",
        "op",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticEnvConditionFormula:
        """Build and return the DiagnosticEnvConditionFormula instance with validation."""
        self._validate_instance()
        return self._obj