"""DataPrototypeInPortInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1009)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from abc import ABC, abstractmethod


class DataPrototypeInPortInterfaceInstanceRef(ARObject, ABC):
    """AUTOSAR DataPrototypeInPortInterfaceInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    abstract_base: Optional[PortInterface]
    context_datas: list[Any]
    root_data_ref: Optional[ARRef]
    target_data_ref: ARRef
    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceInstanceRef."""
        super().__init__()
        self.abstract_base: Optional[PortInterface] = None
        self.context_datas: list[Any] = []
        self.root_data_ref: Optional[ARRef] = None
        self.target_data_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeInPortInterfaceInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize abstract_base
        if self.abstract_base is not None:
            serialized = ARObject._serialize_item(self.abstract_base, "PortInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ABSTRACT-BASE")
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

        # Serialize root_data_ref
        if self.root_data_ref is not None:
            serialized = ARObject._serialize_item(self.root_data_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data_ref
        if self.target_data_ref is not None:
            serialized = ARObject._serialize_item(self.target_data_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInPortInterfaceInstanceRef":
        """Deserialize XML element to DataPrototypeInPortInterfaceInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInPortInterfaceInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse abstract_base
        child = ARObject._find_child_element(element, "ABSTRACT-BASE")
        if child is not None:
            abstract_base_value = ARObject._deserialize_by_tag(child, "PortInterface")
            obj.abstract_base = abstract_base_value

        # Parse context_datas (list from container "CONTEXT-DATAS")
        obj.context_datas = []
        container = ARObject._find_child_element(element, "CONTEXT-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_datas.append(child_value)

        # Parse root_data_ref
        child = ARObject._find_child_element(element, "ROOT-DATA-REF")
        if child is not None:
            root_data_ref_value = ARRef.deserialize(child)
            obj.root_data_ref = root_data_ref_value

        # Parse target_data_ref
        child = ARObject._find_child_element(element, "TARGET-DATA-REF")
        if child is not None:
            target_data_ref_value = ARRef.deserialize(child)
            obj.target_data_ref = target_data_ref_value

        return obj



class DataPrototypeInPortInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInPortInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInPortInterfaceInstanceRef = DataPrototypeInPortInterfaceInstanceRef()

    def build(self) -> DataPrototypeInPortInterfaceInstanceRef:
        """Build and return DataPrototypeInPortInterfaceInstanceRef object.

        Returns:
            DataPrototypeInPortInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
