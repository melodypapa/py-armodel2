"""RoleBasedDataAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 226)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 607)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)


class RoleBasedDataAssignment(ARObject):
    """AUTOSAR RoleBasedDataAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    role: Optional[Identifier]
    used_data_ref: Optional[ARRef]
    used_parameter_ref: Optional[ARRef]
    used_pim_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RoleBasedDataAssignment."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.used_data_ref: Optional[ARRef] = None
        self.used_parameter_ref: Optional[ARRef] = None
        self.used_pim_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RoleBasedDataAssignment to XML element.

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

        # Serialize used_data_ref
        if self.used_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.used_data_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize used_parameter_ref
        if self.used_parameter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.used_parameter_ref, "AutosarParameterRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-PARAMETER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize used_pim_ref
        if self.used_pim_ref is not None:
            serialized = SerializationHelper.serialize_item(self.used_pim_ref, "PerInstanceMemory")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-PIM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedDataAssignment":
        """Deserialize XML element to RoleBasedDataAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedDataAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse role
        child = SerializationHelper.find_child_element(element, "ROLE")
        if child is not None:
            role_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse used_data_ref
        child = SerializationHelper.find_child_element(element, "USED-DATA-REF")
        if child is not None:
            used_data_ref_value = ARRef.deserialize(child)
            obj.used_data_ref = used_data_ref_value

        # Parse used_parameter_ref
        child = SerializationHelper.find_child_element(element, "USED-PARAMETER-REF")
        if child is not None:
            used_parameter_ref_value = ARRef.deserialize(child)
            obj.used_parameter_ref = used_parameter_ref_value

        # Parse used_pim_ref
        child = SerializationHelper.find_child_element(element, "USED-PIM-REF")
        if child is not None:
            used_pim_ref_value = ARRef.deserialize(child)
            obj.used_pim_ref = used_pim_ref_value

        return obj



class RoleBasedDataAssignmentBuilder:
    """Builder for RoleBasedDataAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedDataAssignment = RoleBasedDataAssignment()

    def build(self) -> RoleBasedDataAssignment:
        """Build and return RoleBasedDataAssignment object.

        Returns:
            RoleBasedDataAssignment instance
        """
        # TODO: Add validation
        return self._obj
