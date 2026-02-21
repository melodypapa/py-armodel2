"""DiagnosticComControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control import (
    DiagnosticComControl,
)


class DiagnosticComControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticComControlClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    all_channelse_refs: list[ARRef]
    all_physical_refs: list[Any]
    specific_channels: list[DiagnosticComControl]
    sub_nodes: list[DiagnosticComControl]
    def __init__(self) -> None:
        """Initialize DiagnosticComControlClass."""
        super().__init__()
        self.all_channelse_refs: list[ARRef] = []
        self.all_physical_refs: list[Any] = []
        self.specific_channels: list[DiagnosticComControl] = []
        self.sub_nodes: list[DiagnosticComControl] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControlClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticComControlClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize all_channelse_refs (list to container "ALL-CHANNELSE-REFS")
        if self.all_channelse_refs:
            wrapper = ET.Element("ALL-CHANNELSE-REFS")
            for item in self.all_channelse_refs:
                serialized = SerializationHelper.serialize_item(item, "CommunicationCluster")
                if serialized is not None:
                    child_elem = ET.Element("ALL-CHANNELSE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize all_physical_refs (list to container "ALL-PHYSICAL-REFS")
        if self.all_physical_refs:
            wrapper = ET.Element("ALL-PHYSICAL-REFS")
            for item in self.all_physical_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("ALL-PHYSICAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize specific_channels (list to container "SPECIFIC-CHANNELS")
        if self.specific_channels:
            wrapper = ET.Element("SPECIFIC-CHANNELS")
            for item in self.specific_channels:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticComControl")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sub_nodes (list to container "SUB-NODES")
        if self.sub_nodes:
            wrapper = ET.Element("SUB-NODES")
            for item in self.sub_nodes:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticComControl")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlClass":
        """Deserialize XML element to DiagnosticComControlClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControlClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticComControlClass, cls).deserialize(element)

        # Parse all_channelse_refs (list from container "ALL-CHANNELSE-REFS")
        obj.all_channelse_refs = []
        container = SerializationHelper.find_child_element(element, "ALL-CHANNELSE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.all_channelse_refs.append(child_value)

        # Parse all_physical_refs (list from container "ALL-PHYSICAL-REFS")
        obj.all_physical_refs = []
        container = SerializationHelper.find_child_element(element, "ALL-PHYSICAL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.all_physical_refs.append(child_value)

        # Parse specific_channels (list from container "SPECIFIC-CHANNELS")
        obj.specific_channels = []
        container = SerializationHelper.find_child_element(element, "SPECIFIC-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.specific_channels.append(child_value)

        # Parse sub_nodes (list from container "SUB-NODES")
        obj.sub_nodes = []
        container = SerializationHelper.find_child_element(element, "SUB-NODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_nodes.append(child_value)

        return obj



class DiagnosticComControlClassBuilder:
    """Builder for DiagnosticComControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlClass = DiagnosticComControlClass()

    def build(self) -> DiagnosticComControlClass:
        """Build and return DiagnosticComControlClass object.

        Returns:
            DiagnosticComControlClass instance
        """
        # TODO: Add validation
        return self._obj
