"""BswModeReceiverPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group_prototype import (
    ModeDeclarationGroupPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswModeReceiverPolicy(ARObject):
    """AUTOSAR BswModeReceiverPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-MODE-RECEIVER-POLICY"


    enhanced_mode_api: Optional[Boolean]
    required_mode_group_ref: Optional[ARRef]
    supports_asynchronous_mode_switch: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ENHANCED-MODE-API": lambda obj, elem: setattr(obj, "enhanced_mode_api", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "REQUIRED-MODE-GROUP-REF": lambda obj, elem: setattr(obj, "required_mode_group_ref", ARRef.deserialize(elem)),
        "SUPPORTS-ASYNCHRONOUS-MODE-SWITCH": lambda obj, elem: setattr(obj, "supports_asynchronous_mode_switch", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize BswModeReceiverPolicy."""
        super().__init__()
        self.enhanced_mode_api: Optional[Boolean] = None
        self.required_mode_group_ref: Optional[ARRef] = None
        self.supports_asynchronous_mode_switch: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModeReceiverPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModeReceiverPolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize enhanced_mode_api
        if self.enhanced_mode_api is not None:
            serialized = SerializationHelper.serialize_item(self.enhanced_mode_api, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENHANCED-MODE-API")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required_mode_group_ref
        if self.required_mode_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.required_mode_group_ref, "ModeDeclarationGroupPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-MODE-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize supports_asynchronous_mode_switch
        if self.supports_asynchronous_mode_switch is not None:
            serialized = SerializationHelper.serialize_item(self.supports_asynchronous_mode_switch, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORTS-ASYNCHRONOUS-MODE-SWITCH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeReceiverPolicy":
        """Deserialize XML element to BswModeReceiverPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModeReceiverPolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModeReceiverPolicy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ENHANCED-MODE-API":
                setattr(obj, "enhanced_mode_api", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "REQUIRED-MODE-GROUP-REF":
                setattr(obj, "required_mode_group_ref", ARRef.deserialize(child))
            elif tag == "SUPPORTS-ASYNCHRONOUS-MODE-SWITCH":
                setattr(obj, "supports_asynchronous_mode_switch", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class BswModeReceiverPolicyBuilder(BuilderBase):
    """Builder for BswModeReceiverPolicy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModeReceiverPolicy = BswModeReceiverPolicy()


    def with_enhanced_mode_api(self, value: Optional[Boolean]) -> "BswModeReceiverPolicyBuilder":
        """Set enhanced_mode_api attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enhanced_mode_api = value
        return self

    def with_required_mode_group(self, value: Optional[ModeDeclarationGroupPrototype]) -> "BswModeReceiverPolicyBuilder":
        """Set required_mode_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.required_mode_group = value
        return self

    def with_supports_asynchronous_mode_switch(self, value: Optional[Boolean]) -> "BswModeReceiverPolicyBuilder":
        """Set supports_asynchronous_mode_switch attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.supports_asynchronous_mode_switch = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "enhancedModeApi",
        "requiredModeGroup",
        "supportsAsynchronousModeSwitch",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswModeReceiverPolicy:
        """Build and return the BswModeReceiverPolicy instance with validation."""
        self._validate_instance()
        return self._obj