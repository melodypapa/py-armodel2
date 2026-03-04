"""CompuScaleRationalFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import CompuScaleContentsBuilder
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_rational_coeffs import (
    CompuRationalCoeffs,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CompuScaleRationalFormula(CompuScaleContents):
    """AUTOSAR CompuScaleRationalFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COMPU-SCALE-RATIONAL-FORMULA"


    compu_rational_coeffs: Optional[CompuRationalCoeffs]
    _DESERIALIZE_DISPATCH = {
        "COMPU-RATIONAL-COEFFS": lambda obj, elem: setattr(obj, "compu_rational_coeffs", SerializationHelper.deserialize_by_tag(elem, "CompuRationalCoeffs")),
    }


    def __init__(self) -> None:
        """Initialize CompuScaleRationalFormula."""
        super().__init__()
        self.compu_rational_coeffs: Optional[CompuRationalCoeffs] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuScaleRationalFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompuScaleRationalFormula, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_rational_coeffs
        if self.compu_rational_coeffs is not None:
            serialized = SerializationHelper.serialize_item(self.compu_rational_coeffs, "CompuRationalCoeffs")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-RATIONAL-COEFFS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScaleRationalFormula":
        """Deserialize XML element to CompuScaleRationalFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScaleRationalFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompuScaleRationalFormula, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMPU-RATIONAL-COEFFS":
                setattr(obj, "compu_rational_coeffs", SerializationHelper.deserialize_by_tag(child, "CompuRationalCoeffs"))

        return obj



class CompuScaleRationalFormulaBuilder(CompuScaleContentsBuilder):
    """Builder for CompuScaleRationalFormula with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CompuScaleRationalFormula = CompuScaleRationalFormula()


    def with_compu_rational_coeffs(self, value: Optional[CompuRationalCoeffs]) -> "CompuScaleRationalFormulaBuilder":
        """Set compu_rational_coeffs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.compu_rational_coeffs = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "compuRationalCoeffs",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CompuScaleRationalFormula:
        """Build and return the CompuScaleRationalFormula instance with validation."""
        self._validate_instance()
        return self._obj