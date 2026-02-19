"""DataPrototypeInSenderReceiverInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 788)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.data_prototype_in_port_interface_instance_ref import (
    DataPrototypeInPortInterfaceInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInSenderReceiverInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """AUTOSAR DataPrototypeInSenderReceiverInterfaceInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_interface: Optional[Any]
    context_datas: list[Any]
    root_data_prototype_in_sr_ref: Optional[ARRef]
    target_data_prototype_in_sr_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeInSenderReceiverInterfaceInstanceRef."""
        super().__init__()
        self.base_interface: Optional[Any] = None
        self.context_datas: list[Any] = []
        self.root_data_prototype_in_sr_ref: Optional[ARRef] = None
        self.target_data_prototype_in_sr_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeInSenderReceiverInterfaceInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeInSenderReceiverInterfaceInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_interface
        if self.base_interface is not None:
            serialized = ARObject._serialize_item(self.base_interface, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-INTERFACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_datas (list to container "CONTEXT-DATAS")
        if self.context_datas:
            wrapper = ET.Element("CONTEXT-DATAS")
            for item in self.context_datas:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize root_data_prototype_in_sr_ref
        if self.root_data_prototype_in_sr_ref is not None:
            serialized = ARObject._serialize_item(self.root_data_prototype_in_sr_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-DATA-PROTOTYPE-IN-SR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data_prototype_in_sr_ref
        if self.target_data_prototype_in_sr_ref is not None:
            serialized = ARObject._serialize_item(self.target_data_prototype_in_sr_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA-PROTOTYPE-IN-SR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """Deserialize XML element to DataPrototypeInSenderReceiverInterfaceInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInSenderReceiverInterfaceInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeInSenderReceiverInterfaceInstanceRef, cls).deserialize(element)

        # Parse base_interface
        child = ARObject._find_child_element(element, "BASE-INTERFACE")
        if child is not None:
            base_interface_value = child.text
            obj.base_interface = base_interface_value

        # Parse context_datas (list from container "CONTEXT-DATAS")
        obj.context_datas = []
        container = ARObject._find_child_element(element, "CONTEXT-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_datas.append(child_value)

        # Parse root_data_prototype_in_sr_ref
        child = ARObject._find_child_element(element, "ROOT-DATA-PROTOTYPE-IN-SR")
        if child is not None:
            root_data_prototype_in_sr_ref_value = ARObject._deserialize_by_tag(child, "AutosarDataPrototype")
            obj.root_data_prototype_in_sr_ref = root_data_prototype_in_sr_ref_value

        # Parse target_data_prototype_in_sr_ref
        child = ARObject._find_child_element(element, "TARGET-DATA-PROTOTYPE-IN-SR")
        if child is not None:
            target_data_prototype_in_sr_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.target_data_prototype_in_sr_ref = target_data_prototype_in_sr_ref_value

        return obj



class DataPrototypeInSenderReceiverInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInSenderReceiverInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInSenderReceiverInterfaceInstanceRef = DataPrototypeInSenderReceiverInterfaceInstanceRef()

    def build(self) -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
        """Build and return DataPrototypeInSenderReceiverInterfaceInstanceRef object.

        Returns:
            DataPrototypeInSenderReceiverInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
