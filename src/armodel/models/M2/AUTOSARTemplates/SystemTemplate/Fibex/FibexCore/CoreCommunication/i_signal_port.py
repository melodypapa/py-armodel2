"""ISignalPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 305)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleInvalidEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)


class ISignalPort(CommConnectorPort):
    """AUTOSAR ISignalPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_filter: Optional[DataFilter]
    dds_qos_profile_ref: Optional[ARRef]
    first_timeout: Optional[TimeValue]
    handle_invalid_enum: Optional[HandleInvalidEnum]
    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize ISignalPort."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.dds_qos_profile_ref: Optional[ARRef] = None
        self.first_timeout: Optional[TimeValue] = None
        self.handle_invalid_enum: Optional[HandleInvalidEnum] = None
        self.timeout: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize ISignalPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_filter
        if self.data_filter is not None:
            serialized = ARObject._serialize_item(self.data_filter, "DataFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_qos_profile_ref
        if self.dds_qos_profile_ref is not None:
            serialized = ARObject._serialize_item(self.dds_qos_profile_ref, "DdsCpQosProfile")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-QOS-PROFILE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize first_timeout
        if self.first_timeout is not None:
            serialized = ARObject._serialize_item(self.first_timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_invalid_enum
        if self.handle_invalid_enum is not None:
            serialized = ARObject._serialize_item(self.handle_invalid_enum, "HandleInvalidEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-INVALID-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout
        if self.timeout is not None:
            serialized = ARObject._serialize_item(self.timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalPort":
        """Deserialize XML element to ISignalPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalPort, cls).deserialize(element)

        # Parse data_filter
        child = ARObject._find_child_element(element, "DATA-FILTER")
        if child is not None:
            data_filter_value = ARObject._deserialize_by_tag(child, "DataFilter")
            obj.data_filter = data_filter_value

        # Parse dds_qos_profile_ref
        child = ARObject._find_child_element(element, "DDS-QOS-PROFILE-REF")
        if child is not None:
            dds_qos_profile_ref_value = ARRef.deserialize(child)
            obj.dds_qos_profile_ref = dds_qos_profile_ref_value

        # Parse first_timeout
        child = ARObject._find_child_element(element, "FIRST-TIMEOUT")
        if child is not None:
            first_timeout_value = child.text
            obj.first_timeout = first_timeout_value

        # Parse handle_invalid_enum
        child = ARObject._find_child_element(element, "HANDLE-INVALID-ENUM")
        if child is not None:
            handle_invalid_enum_value = HandleInvalidEnum.deserialize(child)
            obj.handle_invalid_enum = handle_invalid_enum_value

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = child.text
            obj.timeout = timeout_value

        return obj



class ISignalPortBuilder:
    """Builder for ISignalPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalPort = ISignalPort()

    def build(self) -> ISignalPort:
        """Build and return ISignalPort object.

        Returns:
            ISignalPort instance
        """
        # TODO: Add validation
        return self._obj
