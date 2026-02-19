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

    all_channelses: list[CommunicationCluster]
    all_physicals: list[Any]
    specific_channels: list[DiagnosticComControl]
    sub_nodes: list[DiagnosticComControl]
    def __init__(self) -> None:
        """Initialize DiagnosticComControlClass."""
        super().__init__()
        self.all_channelses: list[CommunicationCluster] = []
        self.all_physicals: list[Any] = []
        self.specific_channels: list[DiagnosticComControl] = []
        self.sub_nodes: list[DiagnosticComControl] = []
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControlClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticComControlClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize all_channelses (list to container "ALL-CHANNELSES")
        if self.all_channelses:
            wrapper = ET.Element("ALL-CHANNELSES")
            for item in self.all_channelses:
                serialized = ARObject._serialize_item(item, "CommunicationCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize all_physicals (list to container "ALL-PHYSICALS")
        if self.all_physicals:
            wrapper = ET.Element("ALL-PHYSICALS")
            for item in self.all_physicals:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize specific_channels (list to container "SPECIFIC-CHANNELS")
        if self.specific_channels:
            wrapper = ET.Element("SPECIFIC-CHANNELS")
            for item in self.specific_channels:
                serialized = ARObject._serialize_item(item, "DiagnosticComControl")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sub_nodes (list to container "SUB-NODES")
        if self.sub_nodes:
            wrapper = ET.Element("SUB-NODES")
            for item in self.sub_nodes:
                serialized = ARObject._serialize_item(item, "DiagnosticComControl")
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

        # Parse all_channelses (list from container "ALL-CHANNELSES")
        obj.all_channelses = []
        container = ARObject._find_child_element(element, "ALL-CHANNELSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.all_channelses.append(child_value)

        # Parse all_physicals (list from container "ALL-PHYSICALS")
        obj.all_physicals = []
        container = ARObject._find_child_element(element, "ALL-PHYSICALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.all_physicals.append(child_value)

        # Parse specific_channels (list from container "SPECIFIC-CHANNELS")
        obj.specific_channels = []
        container = ARObject._find_child_element(element, "SPECIFIC-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.specific_channels.append(child_value)

        # Parse sub_nodes (list from container "SUB-NODES")
        obj.sub_nodes = []
        container = ARObject._find_child_element(element, "SUB-NODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
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
