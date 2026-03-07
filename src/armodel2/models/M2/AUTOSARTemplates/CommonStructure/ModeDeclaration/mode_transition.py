"""ModeTransition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 43)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 630)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeTransition(Identifiable):
    """AUTOSAR ModeTransition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-TRANSITION"


    entered_mode_ref: Optional[ARRef]
    exited_mode_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ENTERED-MODE-REF": lambda obj, elem: setattr(obj, "entered_mode_ref", ARRef.deserialize(elem)),
        "EXITED-MODE-REF": lambda obj, elem: setattr(obj, "exited_mode_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ModeTransition."""
        super().__init__()
        self.entered_mode_ref: Optional[ARRef] = None
        self.exited_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeTransition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeTransition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize entered_mode_ref
        if self.entered_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.entered_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENTERED-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize exited_mode_ref
        if self.exited_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.exited_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXITED-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeTransition":
        """Deserialize XML element to ModeTransition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeTransition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeTransition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ENTERED-MODE-REF":
                setattr(obj, "entered_mode_ref", ARRef.deserialize(child))
            elif tag == "EXITED-MODE-REF":
                setattr(obj, "exited_mode_ref", ARRef.deserialize(child))

        return obj



class ModeTransitionBuilder(IdentifiableBuilder):
    """Builder for ModeTransition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeTransition = ModeTransition()


    def with_entered_mode(self, value: Optional[ModeDeclaration]) -> "ModeTransitionBuilder":
        """Set entered_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'entered_mode' is required and cannot be None")
        self._obj.entered_mode = value
        return self

    def with_exited_mode(self, value: Optional[ModeDeclaration]) -> "ModeTransitionBuilder":
        """Set exited_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'exited_mode' is required and cannot be None")
        self._obj.exited_mode = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "enteredMode",
        "exitedMode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModeTransition:
        """Build and return the ModeTransition instance with validation."""
        self._validate_instance()
        return self._obj