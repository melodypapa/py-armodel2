"""RoleBasedDataTypeAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 227)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 610)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)


class RoleBasedDataTypeAssignment(ARObject):
    """AUTOSAR RoleBasedDataTypeAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    role: Optional[Identifier]
    used_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize RoleBasedDataTypeAssignment."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.used_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize RoleBasedDataTypeAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Serialize used_ref
        if self.used_ref is not None:
            serialized = SerializationHelper.serialize_item(self.used_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedDataTypeAssignment":
        """Deserialize XML element to RoleBasedDataTypeAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedDataTypeAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse role
        child = SerializationHelper.find_child_element(element, "ROLE")
        if child is not None:
            role_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse used_ref
        child = SerializationHelper.find_child_element(element, "USED-REF")
        if child is not None:
            used_ref_value = ARRef.deserialize(child)
            obj.used_ref = used_ref_value

        return obj



class RoleBasedDataTypeAssignmentBuilder:
    """Builder for RoleBasedDataTypeAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedDataTypeAssignment = RoleBasedDataTypeAssignment()

    def build(self) -> RoleBasedDataTypeAssignment:
        """Build and return RoleBasedDataTypeAssignment object.

        Returns:
            RoleBasedDataTypeAssignment instance
        """
        # TODO: Add validation
        return self._obj
