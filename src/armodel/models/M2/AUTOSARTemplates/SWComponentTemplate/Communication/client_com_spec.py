"""ClientComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientComSpec(RPortComSpec):
    """AUTOSAR ClientComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    end_to_end_call: Optional[TimeValue]
    operation_ref: Optional[ARRef]
    transformation_coms: list[Any]
    def __init__(self) -> None:
        """Initialize ClientComSpec."""
        super().__init__()
        self.end_to_end_call: Optional[TimeValue] = None
        self.operation_ref: Optional[ARRef] = None
        self.transformation_coms: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize end_to_end_call
        if self.end_to_end_call is not None:
            serialized = SerializationHelper.serialize_item(self.end_to_end_call, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("END-TO-END-CALL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize operation_ref
        if self.operation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.operation_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_coms (list to container "TRANSFORMATION-COMS")
        if self.transformation_coms:
            wrapper = ET.Element("TRANSFORMATION-COMS")
            for item in self.transformation_coms:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientComSpec":
        """Deserialize XML element to ClientComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientComSpec, cls).deserialize(element)

        # Parse end_to_end_call
        child = SerializationHelper.find_child_element(element, "END-TO-END-CALL")
        if child is not None:
            end_to_end_call_value = child.text
            obj.end_to_end_call = end_to_end_call_value

        # Parse operation_ref
        child = SerializationHelper.find_child_element(element, "OPERATION-REF")
        if child is not None:
            operation_ref_value = ARRef.deserialize(child)
            obj.operation_ref = operation_ref_value

        # Parse transformation_coms (list from container "TRANSFORMATION-COMS")
        obj.transformation_coms = []
        container = SerializationHelper.find_child_element(element, "TRANSFORMATION-COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformation_coms.append(child_value)

        return obj



class ClientComSpecBuilder:
    """Builder for ClientComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientComSpec = ClientComSpec()

    def build(self) -> ClientComSpec:
        """Build and return ClientComSpec object.

        Returns:
            ClientComSpec instance
        """
        # TODO: Add validation
        return self._obj
