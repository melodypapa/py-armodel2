"""RoleBasedBswModuleEntryAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 226)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class RoleBasedBswModuleEntryAssignment(ARObject):
    """AUTOSAR RoleBasedBswModuleEntryAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_entry_ref: Optional[ARRef]
    role: Optional[Identifier]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse assigned_entry_ref
        child = SerializationHelper.find_child_element(element, "ASSIGNED-ENTRY-REF")
        if child is not None:
            assigned_entry_ref_value = ARRef.deserialize(child)
            obj.assigned_entry_ref = assigned_entry_ref_value

        # Parse role
        child = SerializationHelper.find_child_element(element, "ROLE")
        if child is not None:
            role_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        return obj



class RoleBasedBswModuleEntryAssignmentBuilder:
    """Builder for RoleBasedBswModuleEntryAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedBswModuleEntryAssignment = RoleBasedBswModuleEntryAssignment()

    def build(self) -> RoleBasedBswModuleEntryAssignment:
        """Build and return RoleBasedBswModuleEntryAssignment object.

        Returns:
            RoleBasedBswModuleEntryAssignment instance
        """
        # TODO: Add validation
        return self._obj
