"""PortElementToCommunicationResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 905)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class PortElementToCommunicationResourceMapping(Identifiable):
    """AUTOSAR PortElementToCommunicationResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_server_instance_ref: Optional[ClientServerOperation]
    communication: Optional[CpSoftwareCluster]
    mode_ref: Optional[ARRef]
    parameter_data_in_system_instance_ref: Optional[ARRef]
    trigger_ref: Optional[ARRef]
    variable_data_system_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PortElementToCommunicationResourceMapping."""
        super().__init__()
        self.client_server_instance_ref: Optional[ClientServerOperation] = None
        self.communication: Optional[CpSoftwareCluster] = None
        self.mode_ref: Optional[ARRef] = None
        self.parameter_data_in_system_instance_ref: Optional[ARRef] = None
        self.trigger_ref: Optional[ARRef] = None
        self.variable_data_system_instance_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize PortElementToCommunicationResourceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortElementToCommunicationResourceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_server_instance_ref
        if self.client_server_instance_ref is not None:
            serialized = ARObject._serialize_item(self.client_server_instance_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-SERVER-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize communication
        if self.communication is not None:
            serialized = ARObject._serialize_item(self.communication, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_ref
        if self.mode_ref is not None:
            serialized = ARObject._serialize_item(self.mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter_data_in_system_instance_ref
        if self.parameter_data_in_system_instance_ref is not None:
            serialized = ARObject._serialize_item(self.parameter_data_in_system_instance_ref, "ParameterDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER-DATA-IN-SYSTEM-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = ARObject._serialize_item(self.trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_data_system_instance_ref
        if self.variable_data_system_instance_ref is not None:
            serialized = ARObject._serialize_item(self.variable_data_system_instance_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-DATA-SYSTEM-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortElementToCommunicationResourceMapping":
        """Deserialize XML element to PortElementToCommunicationResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortElementToCommunicationResourceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortElementToCommunicationResourceMapping, cls).deserialize(element)

        # Parse client_server_instance_ref
        child = ARObject._find_child_element(element, "CLIENT-SERVER-INSTANCE-REF")
        if child is not None:
            client_server_instance_ref_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.client_server_instance_ref = client_server_instance_ref_value

        # Parse communication
        child = ARObject._find_child_element(element, "COMMUNICATION")
        if child is not None:
            communication_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.communication = communication_value

        # Parse mode_ref
        child = ARObject._find_child_element(element, "MODE")
        if child is not None:
            mode_ref_value = ARRef.deserialize(child)
            obj.mode_ref = mode_ref_value

        # Parse parameter_data_in_system_instance_ref
        child = ARObject._find_child_element(element, "PARAMETER-DATA-IN-SYSTEM-INSTANCE-REF")
        if child is not None:
            parameter_data_in_system_instance_ref_value = ARRef.deserialize(child)
            obj.parameter_data_in_system_instance_ref = parameter_data_in_system_instance_ref_value

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = ARRef.deserialize(child)
            obj.trigger_ref = trigger_ref_value

        # Parse variable_data_system_instance_ref
        child = ARObject._find_child_element(element, "VARIABLE-DATA-SYSTEM-INSTANCE-REF")
        if child is not None:
            variable_data_system_instance_ref_value = ARRef.deserialize(child)
            obj.variable_data_system_instance_ref = variable_data_system_instance_ref_value

        return obj



class PortElementToCommunicationResourceMappingBuilder:
    """Builder for PortElementToCommunicationResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortElementToCommunicationResourceMapping = PortElementToCommunicationResourceMapping()

    def build(self) -> PortElementToCommunicationResourceMapping:
        """Build and return PortElementToCommunicationResourceMapping object.

        Returns:
            PortElementToCommunicationResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
