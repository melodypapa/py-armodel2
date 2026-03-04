"""ModeInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import PortInterfaceMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR ModeInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-INTERFACE-MAPPING"


    mode_mapping_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MODE-MAPPING-REF": lambda obj, elem: setattr(obj, "mode_mapping_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ModeInterfaceMapping."""
        super().__init__()
        self.mode_mapping_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeInterfaceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeInterfaceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_mapping_ref
        if self.mode_mapping_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_mapping_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-MAPPING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeInterfaceMapping":
        """Deserialize XML element to ModeInterfaceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeInterfaceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeInterfaceMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MODE-MAPPING-REF":
                setattr(obj, "mode_mapping_ref", ARRef.deserialize(child))

        return obj



class ModeInterfaceMappingBuilder(PortInterfaceMappingBuilder):
    """Builder for ModeInterfaceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeInterfaceMapping = ModeInterfaceMapping()


    def with_mode_mapping(self, value: Optional[ModeDeclarationGroup]) -> "ModeInterfaceMappingBuilder":
        """Set mode_mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode_mapping = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "modeMapping",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModeInterfaceMapping:
        """Build and return the ModeInterfaceMapping instance with validation."""
        self._validate_instance()
        return self._obj