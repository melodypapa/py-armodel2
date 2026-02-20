"""DataPrototypeInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 368)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class DataPrototypeInSystemInstanceRef(ARObject):
    """AUTOSAR DataPrototypeInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[System]
    contexts: list[Any]
    context_datas: list[Any]
    context_port_ref: Optional[ARRef]
    context_root: Optional[RootSwCompositionPrototype]
    root_data_prototype_ref: Optional[ARRef]
    target_data_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.contexts: list[Any] = []
        self.context_datas: list[Any] = []
        self.context_port_ref: Optional[ARRef] = None
        self.context_root: Optional[RootSwCompositionPrototype] = None
        self.root_data_prototype_ref: Optional[ARRef] = None
        self.target_data_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize base
        if self.base is not None:
            serialized = ARObject._serialize_item(self.base, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize contexts (list to container "CONTEXTS")
        if self.contexts:
            wrapper = ET.Element("CONTEXTS")
            for item in self.contexts:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize context_datas (list to container "CONTEXT-DATAS")
        if self.context_datas:
            wrapper = ET.Element("CONTEXT-DATAS")
            for item in self.context_datas:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize context_port_ref
        if self.context_port_ref is not None:
            serialized = ARObject._serialize_item(self.context_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_root
        if self.context_root is not None:
            serialized = ARObject._serialize_item(self.context_root, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-ROOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize root_data_prototype_ref
        if self.root_data_prototype_ref is not None:
            serialized = ARObject._serialize_item(self.root_data_prototype_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-DATA-PROTOTYPE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInSystemInstanceRef":
        """Deserialize XML element to DataPrototypeInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInSystemInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "System")
            obj.base = base_value

        # Parse contexts (list from container "CONTEXTS")
        obj.contexts = []
        container = ARObject._find_child_element(element, "CONTEXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contexts.append(child_value)

        # Parse context_datas (list from container "CONTEXT-DATAS")
        obj.context_datas = []
        container = ARObject._find_child_element(element, "CONTEXT-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_datas.append(child_value)

        # Parse context_port_ref
        child = ARObject._find_child_element(element, "CONTEXT-PORT-REF")
        if child is not None:
            context_port_ref_value = ARRef.deserialize(child)
            obj.context_port_ref = context_port_ref_value

        # Parse context_root
        child = ARObject._find_child_element(element, "CONTEXT-ROOT")
        if child is not None:
            context_root_value = ARObject._deserialize_by_tag(child, "RootSwCompositionPrototype")
            obj.context_root = context_root_value

        # Parse root_data_prototype_ref
        child = ARObject._find_child_element(element, "ROOT-DATA-PROTOTYPE-REF")
        if child is not None:
            root_data_prototype_ref_value = ARRef.deserialize(child)
            obj.root_data_prototype_ref = root_data_prototype_ref_value

        # Parse target_data_ref
        child = ARObject._find_child_element(element, "TARGET-DATA-REF")
        if child is not None:
            target_data_ref_value = ARRef.deserialize(child)
            obj.target_data_ref = target_data_ref_value

        return obj



class DataPrototypeInSystemInstanceRefBuilder:
    """Builder for DataPrototypeInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInSystemInstanceRef = DataPrototypeInSystemInstanceRef()

    def build(self) -> DataPrototypeInSystemInstanceRef:
        """Build and return DataPrototypeInSystemInstanceRef object.

        Returns:
            DataPrototypeInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
