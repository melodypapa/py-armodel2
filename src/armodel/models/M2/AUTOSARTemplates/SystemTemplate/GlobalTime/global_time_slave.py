"""GlobalTimeSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 860)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from abc import ABC, abstractmethod


class GlobalTimeSlave(Identifiable, ABC):
    """AUTOSAR GlobalTimeSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_connector_ref: Optional[ARRef]
    follow_up_timeout_value: Optional[TimeValue]
    icv_verification: Optional[Any]
    time_leap_future: Optional[TimeValue]
    time_leap: Optional[PositiveInteger]
    time_leap_past: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeSlave."""
        super().__init__()
        self.communication_connector_ref: Optional[ARRef] = None
        self.follow_up_timeout_value: Optional[TimeValue] = None
        self.icv_verification: Optional[Any] = None
        self.time_leap_future: Optional[TimeValue] = None
        self.time_leap: Optional[PositiveInteger] = None
        self.time_leap_past: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeSlave to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeSlave, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_connector_ref
        if self.communication_connector_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_connector_ref, "CommunicationConnector")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CONNECTOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize follow_up_timeout_value
        if self.follow_up_timeout_value is not None:
            serialized = SerializationHelper.serialize_item(self.follow_up_timeout_value, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FOLLOW-UP-TIMEOUT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize icv_verification
        if self.icv_verification is not None:
            serialized = SerializationHelper.serialize_item(self.icv_verification, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ICV-VERIFICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_leap_future
        if self.time_leap_future is not None:
            serialized = SerializationHelper.serialize_item(self.time_leap_future, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-LEAP-FUTURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_leap
        if self.time_leap is not None:
            serialized = SerializationHelper.serialize_item(self.time_leap, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-LEAP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_leap_past
        if self.time_leap_past is not None:
            serialized = SerializationHelper.serialize_item(self.time_leap_past, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-LEAP-PAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeSlave":
        """Deserialize XML element to GlobalTimeSlave object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeSlave object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeSlave, cls).deserialize(element)

        # Parse communication_connector_ref
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-CONNECTOR-REF")
        if child is not None:
            communication_connector_ref_value = ARRef.deserialize(child)
            obj.communication_connector_ref = communication_connector_ref_value

        # Parse follow_up_timeout_value
        child = SerializationHelper.find_child_element(element, "FOLLOW-UP-TIMEOUT-VALUE")
        if child is not None:
            follow_up_timeout_value_value = child.text
            obj.follow_up_timeout_value = follow_up_timeout_value_value

        # Parse icv_verification
        child = SerializationHelper.find_child_element(element, "ICV-VERIFICATION")
        if child is not None:
            icv_verification_value = child.text
            obj.icv_verification = icv_verification_value

        # Parse time_leap_future
        child = SerializationHelper.find_child_element(element, "TIME-LEAP-FUTURE")
        if child is not None:
            time_leap_future_value = child.text
            obj.time_leap_future = time_leap_future_value

        # Parse time_leap
        child = SerializationHelper.find_child_element(element, "TIME-LEAP")
        if child is not None:
            time_leap_value = child.text
            obj.time_leap = time_leap_value

        # Parse time_leap_past
        child = SerializationHelper.find_child_element(element, "TIME-LEAP-PAST")
        if child is not None:
            time_leap_past_value = child.text
            obj.time_leap_past = time_leap_past_value

        return obj



class GlobalTimeSlaveBuilder:
    """Builder for GlobalTimeSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeSlave = GlobalTimeSlave()

    def build(self) -> GlobalTimeSlave:
        """Build and return GlobalTimeSlave object.

        Returns:
            GlobalTimeSlave instance
        """
        # TODO: Add validation
        return self._obj
