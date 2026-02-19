"""GlobalTimeGateway AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 861)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)


class GlobalTimeGateway(Identifiable):
    """AUTOSAR GlobalTimeGateway."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    host: Optional[EcuInstance]
    master: Optional[GlobalTimeMaster]
    slave: Optional[GlobalTimeSlave]
    def __init__(self) -> None:
        """Initialize GlobalTimeGateway."""
        super().__init__()
        self.host: Optional[EcuInstance] = None
        self.master: Optional[GlobalTimeMaster] = None
        self.slave: Optional[GlobalTimeSlave] = None
    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeGateway to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeGateway, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize host
        if self.host is not None:
            serialized = ARObject._serialize_item(self.host, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HOST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize master
        if self.master is not None:
            serialized = ARObject._serialize_item(self.master, "GlobalTimeMaster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slave
        if self.slave is not None:
            serialized = ARObject._serialize_item(self.slave, "GlobalTimeSlave")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLAVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeGateway":
        """Deserialize XML element to GlobalTimeGateway object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeGateway object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeGateway, cls).deserialize(element)

        # Parse host
        child = ARObject._find_child_element(element, "HOST")
        if child is not None:
            host_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.host = host_value

        # Parse master
        child = ARObject._find_child_element(element, "MASTER")
        if child is not None:
            master_value = ARObject._deserialize_by_tag(child, "GlobalTimeMaster")
            obj.master = master_value

        # Parse slave
        child = ARObject._find_child_element(element, "SLAVE")
        if child is not None:
            slave_value = ARObject._deserialize_by_tag(child, "GlobalTimeSlave")
            obj.slave = slave_value

        return obj



class GlobalTimeGatewayBuilder:
    """Builder for GlobalTimeGateway."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeGateway = GlobalTimeGateway()

    def build(self) -> GlobalTimeGateway:
        """Build and return GlobalTimeGateway object.

        Returns:
            GlobalTimeGateway instance
        """
        # TODO: Add validation
        return self._obj
