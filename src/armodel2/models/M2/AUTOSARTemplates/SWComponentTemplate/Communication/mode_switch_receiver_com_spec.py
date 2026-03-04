"""ModeSwitchReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 191)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import RPortComSpecBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeSwitchReceiverComSpec(RPortComSpec):
    """AUTOSAR ModeSwitchReceiverComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-SWITCH-RECEIVER-COM-SPEC"


    enhanced_mode: Optional[Boolean]
    mode_group_ref: Optional[ARRef]
    supports: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ENHANCED-MODE": lambda obj, elem: setattr(obj, "enhanced_mode", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "MODE-GROUP-REF": lambda obj, elem: setattr(obj, "mode_group_ref", ARRef.deserialize(elem)),
        "SUPPORTS": lambda obj, elem: setattr(obj, "supports", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize ModeSwitchReceiverComSpec."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.mode_group_ref: Optional[ARRef] = None
        self.supports: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeSwitchReceiverComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeSwitchReceiverComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize enhanced_mode
        if self.enhanced_mode is not None:
            serialized = SerializationHelper.serialize_item(self.enhanced_mode, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENHANCED-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_group_ref
        if self.mode_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_group_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize supports
        if self.supports is not None:
            serialized = SerializationHelper.serialize_item(self.supports, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchReceiverComSpec":
        """Deserialize XML element to ModeSwitchReceiverComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchReceiverComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeSwitchReceiverComSpec, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ENHANCED-MODE":
                setattr(obj, "enhanced_mode", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "MODE-GROUP-REF":
                setattr(obj, "mode_group_ref", ARRef.deserialize(child))
            elif tag == "SUPPORTS":
                setattr(obj, "supports", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class ModeSwitchReceiverComSpecBuilder(RPortComSpecBuilder):
    """Builder for ModeSwitchReceiverComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeSwitchReceiverComSpec = ModeSwitchReceiverComSpec()


    def with_enhanced_mode(self, value: Optional[Boolean]) -> "ModeSwitchReceiverComSpecBuilder":
        """Set enhanced_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enhanced_mode = value
        return self

    def with_mode_group(self, value: Optional[ModeDeclarationGroup]) -> "ModeSwitchReceiverComSpecBuilder":
        """Set mode_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode_group = value
        return self

    def with_supports(self, value: Optional[Boolean]) -> "ModeSwitchReceiverComSpecBuilder":
        """Set supports attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.supports = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "enhancedMode",
        "modeGroup",
        "supports",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModeSwitchReceiverComSpec:
        """Build and return the ModeSwitchReceiverComSpec instance with validation."""
        self._validate_instance()
        return self._obj