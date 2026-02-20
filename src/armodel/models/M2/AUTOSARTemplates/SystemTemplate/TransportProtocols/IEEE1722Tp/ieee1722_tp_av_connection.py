"""IEEE1722TpAvConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 639)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod


class IEEE1722TpAvConnection(IEEE1722TpConnection, ABC):
    """AUTOSAR IEEE1722TpAvConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    max_transit_time: Optional[TimeValue]
    sdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAvConnection."""
        super().__init__()
        self.max_transit_time: Optional[TimeValue] = None
        self.sdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAvConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAvConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_transit_time
        if self.max_transit_time is not None:
            serialized = ARObject._serialize_item(self.max_transit_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-TRANSIT-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_refs (list to container "SDU-REFS")
        if self.sdu_refs:
            wrapper = ET.Element("SDU-REFS")
            for item in self.sdu_refs:
                serialized = ARObject._serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("SDU-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAvConnection":
        """Deserialize XML element to IEEE1722TpAvConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAvConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAvConnection, cls).deserialize(element)

        # Parse max_transit_time
        child = ARObject._find_child_element(element, "MAX-TRANSIT-TIME")
        if child is not None:
            max_transit_time_value = child.text
            obj.max_transit_time = max_transit_time_value

        # Parse sdu_refs (list from container "SDU-REFS")
        obj.sdu_refs = []
        container = ARObject._find_child_element(element, "SDU-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdu_refs.append(child_value)

        return obj



class IEEE1722TpAvConnectionBuilder:
    """Builder for IEEE1722TpAvConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAvConnection = IEEE1722TpAvConnection()

    def build(self) -> IEEE1722TpAvConnection:
        """Build and return IEEE1722TpAvConnection object.

        Returns:
            IEEE1722TpAvConnection instance
        """
        # TODO: Add validation
        return self._obj
