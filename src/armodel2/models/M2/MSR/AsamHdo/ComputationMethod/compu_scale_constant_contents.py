"""CompuScaleConstantContents AUTOSAR element.

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
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CompuScaleConstantContents(CompuScaleContents):
    """AUTOSAR CompuScaleConstantContents."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COMPU-SCALE-CONSTANT-CONTENTS"


    compu_const: Optional[CompuConst]
    _DESERIALIZE_DISPATCH = {
        "COMPU-CONST": lambda obj, elem: setattr(obj, "compu_const", SerializationHelper.deserialize_by_tag(elem, "CompuConst")),
    }


    def __init__(self) -> None:
        """Initialize CompuScaleConstantContents."""
        super().__init__()
        self.compu_const: Optional[CompuConst] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuScaleConstantContents to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompuScaleConstantContents, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_const
        if self.compu_const is not None:
            serialized = SerializationHelper.serialize_item(self.compu_const, "CompuConst")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-CONST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScaleConstantContents":
        """Deserialize XML element to CompuScaleConstantContents object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScaleConstantContents object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompuScaleConstantContents, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMPU-CONST":
                setattr(obj, "compu_const", SerializationHelper.deserialize_by_tag(child, "CompuConst"))

        return obj



class CompuScaleConstantContentsBuilder(CompuScaleContentsBuilder):
    """Builder for CompuScaleConstantContents with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CompuScaleConstantContents = CompuScaleConstantContents()


    def with_compu_const(self, value: Optional[CompuConst]) -> "CompuScaleConstantContentsBuilder":
        """Set compu_const attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'compu_const' is required and cannot be None")
        self._obj.compu_const = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "compuConst",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CompuScaleConstantContents:
        """Build and return the CompuScaleConstantContents instance with validation."""
        self._validate_instance()
        return self._obj