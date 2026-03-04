"""ModeErrorBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 44)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 637)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeErrorReactionPolicyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeErrorBehavior(ARObject):
    """AUTOSAR ModeErrorBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-ERROR-BEHAVIOR"


    default_mode_ref: Optional[ARRef]
    error_reaction: Optional[ModeErrorReactionPolicyEnum]
    _DESERIALIZE_DISPATCH = {
        "DEFAULT-MODE-REF": lambda obj, elem: setattr(obj, "default_mode_ref", ARRef.deserialize(elem)),
        "ERROR-REACTION": lambda obj, elem: setattr(obj, "error_reaction", ModeErrorReactionPolicyEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ModeErrorBehavior."""
        super().__init__()
        self.default_mode_ref: Optional[ARRef] = None
        self.error_reaction: Optional[ModeErrorReactionPolicyEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeErrorBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeErrorBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_mode_ref
        if self.default_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.default_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize error_reaction
        if self.error_reaction is not None:
            serialized = SerializationHelper.serialize_item(self.error_reaction, "ModeErrorReactionPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ERROR-REACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeErrorBehavior":
        """Deserialize XML element to ModeErrorBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeErrorBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeErrorBehavior, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEFAULT-MODE-REF":
                setattr(obj, "default_mode_ref", ARRef.deserialize(child))
            elif tag == "ERROR-REACTION":
                setattr(obj, "error_reaction", ModeErrorReactionPolicyEnum.deserialize(child))

        return obj



class ModeErrorBehaviorBuilder(BuilderBase):
    """Builder for ModeErrorBehavior with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeErrorBehavior = ModeErrorBehavior()


    def with_default_mode(self, value: Optional[ModeDeclaration]) -> "ModeErrorBehaviorBuilder":
        """Set default_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_mode = value
        return self

    def with_error_reaction(self, value: Optional[ModeErrorReactionPolicyEnum]) -> "ModeErrorBehaviorBuilder":
        """Set error_reaction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.error_reaction = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "defaultMode",
        "errorReaction",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModeErrorBehavior:
        """Build and return the ModeErrorBehavior instance with validation."""
        self._validate_instance()
        return self._obj