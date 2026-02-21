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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    host_ref: Optional[ARRef]
    master_ref: Optional[ARRef]
    slave_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize GlobalTimeGateway."""
        super().__init__()
        self.host_ref: Optional[ARRef] = None
        self.master_ref: Optional[ARRef] = None
        self.slave_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeGateway to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeGateway, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize host_ref
        if self.host_ref is not None:
            serialized = SerializationHelper.serialize_item(self.host_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HOST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize master_ref
        if self.master_ref is not None:
            serialized = SerializationHelper.serialize_item(self.master_ref, "GlobalTimeMaster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slave_ref
        if self.slave_ref is not None:
            serialized = SerializationHelper.serialize_item(self.slave_ref, "GlobalTimeSlave")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLAVE-REF")
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

        # Parse host_ref
        child = SerializationHelper.find_child_element(element, "HOST-REF")
        if child is not None:
            host_ref_value = ARRef.deserialize(child)
            obj.host_ref = host_ref_value

        # Parse master_ref
        child = SerializationHelper.find_child_element(element, "MASTER-REF")
        if child is not None:
            master_ref_value = ARRef.deserialize(child)
            obj.master_ref = master_ref_value

        # Parse slave_ref
        child = SerializationHelper.find_child_element(element, "SLAVE-REF")
        if child is not None:
            slave_ref_value = ARRef.deserialize(child)
            obj.slave_ref = slave_ref_value

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
