"""ROperationInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 947)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.operation_in_atomic_swc_instance_ref import (
    OperationInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ROperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """AUTOSAR ROperationInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_r_port_prototype_ref: Optional[ARRef]
    target_required_operation_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ROperationInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype_ref: Optional[ARRef] = None
        self.target_required_operation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ROperationInAtomicSwcInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ROperationInAtomicSwcInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_r_port_prototype_ref
        if self.context_r_port_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_r_port_prototype_ref, "AbstractRequiredPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-R-PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_required_operation_ref
        if self.target_required_operation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_required_operation_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-REQUIRED-OPERATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ROperationInAtomicSwcInstanceRef":
        """Deserialize XML element to ROperationInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ROperationInAtomicSwcInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ROperationInAtomicSwcInstanceRef, cls).deserialize(element)

        # Parse context_r_port_prototype_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-R-PORT-PROTOTYPE-REF")
        if child is not None:
            context_r_port_prototype_ref_value = ARRef.deserialize(child)
            obj.context_r_port_prototype_ref = context_r_port_prototype_ref_value

        # Parse target_required_operation_ref
        child = SerializationHelper.find_child_element(element, "TARGET-REQUIRED-OPERATION-REF")
        if child is not None:
            target_required_operation_ref_value = ARRef.deserialize(child)
            obj.target_required_operation_ref = target_required_operation_ref_value

        return obj



class ROperationInAtomicSwcInstanceRefBuilder:
    """Builder for ROperationInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ROperationInAtomicSwcInstanceRef = ROperationInAtomicSwcInstanceRef()

    def build(self) -> ROperationInAtomicSwcInstanceRef:
        """Build and return ROperationInAtomicSwcInstanceRef object.

        Returns:
            ROperationInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
