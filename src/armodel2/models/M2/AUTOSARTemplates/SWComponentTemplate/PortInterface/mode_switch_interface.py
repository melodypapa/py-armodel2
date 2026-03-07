"""ModeSwitchInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 113)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2039)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import PortInterfaceBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group_prototype import (
    ModeDeclarationGroupPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeSwitchInterface(PortInterface):
    """AUTOSAR ModeSwitchInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-SWITCH-INTERFACE"


    mode_group: Optional[ModeDeclarationGroupPrototype]
    _DESERIALIZE_DISPATCH = {
        "MODE-GROUP": lambda obj, elem: setattr(obj, "mode_group", SerializationHelper.deserialize_by_tag(elem, "ModeDeclarationGroupPrototype")),
    }


    def __init__(self) -> None:
        """Initialize ModeSwitchInterface."""
        super().__init__()
        self.mode_group: Optional[ModeDeclarationGroupPrototype] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeSwitchInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeSwitchInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_group
        if self.mode_group is not None:
            serialized = SerializationHelper.serialize_item(self.mode_group, "ModeDeclarationGroupPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchInterface":
        """Deserialize XML element to ModeSwitchInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeSwitchInterface, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MODE-GROUP":
                setattr(obj, "mode_group", SerializationHelper.deserialize_by_tag(child, "ModeDeclarationGroupPrototype"))

        return obj



class ModeSwitchInterfaceBuilder(PortInterfaceBuilder):
    """Builder for ModeSwitchInterface with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeSwitchInterface = ModeSwitchInterface()


    def with_mode_group(self, value: Optional[ModeDeclarationGroupPrototype]) -> "ModeSwitchInterfaceBuilder":
        """Set mode_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'mode_group' is required and cannot be None")
        self._obj.mode_group = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "modeGroup",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModeSwitchInterface:
        """Build and return the ModeSwitchInterface instance with validation."""
        self._validate_instance()
        return self._obj