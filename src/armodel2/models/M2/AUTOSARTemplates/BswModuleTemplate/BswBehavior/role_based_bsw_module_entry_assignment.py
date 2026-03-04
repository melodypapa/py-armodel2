"""RoleBasedBswModuleEntryAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 226)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RoleBasedBswModuleEntryAssignment(ARObject):
    """AUTOSAR RoleBasedBswModuleEntryAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ROLE-BASED-BSW-MODULE-ENTRY-ASSIGNMENT"


    assigned_entry_ref: Optional[ARRef]
    role: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "ASSIGNED-ENTRY-REF": lambda obj, elem: setattr(obj, "assigned_entry_ref", ARRef.deserialize(elem)),
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize RoleBasedBswModuleEntryAssignment."""
        super().__init__()
        self.assigned_entry_ref: Optional[ARRef] = None
        self.role: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RoleBasedBswModuleEntryAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RoleBasedBswModuleEntryAssignment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned_entry_ref
        if self.assigned_entry_ref is not None:
            serialized = SerializationHelper.serialize_item(self.assigned_entry_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNED-ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedBswModuleEntryAssignment":
        """Deserialize XML element to RoleBasedBswModuleEntryAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedBswModuleEntryAssignment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RoleBasedBswModuleEntryAssignment, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ASSIGNED-ENTRY-REF":
                setattr(obj, "assigned_entry_ref", ARRef.deserialize(child))
            elif tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))

        return obj



class RoleBasedBswModuleEntryAssignmentBuilder(BuilderBase):
    """Builder for RoleBasedBswModuleEntryAssignment with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RoleBasedBswModuleEntryAssignment = RoleBasedBswModuleEntryAssignment()


    def with_assigned_entry(self, value: Optional[BswModuleEntry]) -> "RoleBasedBswModuleEntryAssignmentBuilder":
        """Set assigned_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.assigned_entry = value
        return self

    def with_role(self, value: Optional[Identifier]) -> "RoleBasedBswModuleEntryAssignmentBuilder":
        """Set role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.role = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "assignedEntry",
        "role",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RoleBasedBswModuleEntryAssignment:
        """Build and return the RoleBasedBswModuleEntryAssignment instance with validation."""
        self._validate_instance()
        return self._obj