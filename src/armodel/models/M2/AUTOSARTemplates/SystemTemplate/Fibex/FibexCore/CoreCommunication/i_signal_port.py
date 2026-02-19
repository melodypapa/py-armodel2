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
    dds_qos_profile: Optional[DdsCpQosProfile]
    first_timeout: Optional[TimeValue]
    handle_invalid_enum: Optional[HandleInvalidEnum]
    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize ISignalPort."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.dds_qos_profile: Optional[DdsCpQosProfile] = None
        self.first_timeout: Optional[TimeValue] = None
        self.handle_invalid_enum: Optional[HandleInvalidEnum] = None
        self.timeout: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalPort":
        """Deserialize XML element to ISignalPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalPort object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_filter
        child = ARObject._find_child_element(element, "DATA-FILTER")
        if child is not None:
            data_filter_value = ARObject._deserialize_by_tag(child, "DataFilter")
            obj.data_filter = data_filter_value

        # Parse dds_qos_profile
        child = ARObject._find_child_element(element, "DDS-QOS-PROFILE")
        if child is not None:
            dds_qos_profile_value = ARObject._deserialize_by_tag(child, "DdsCpQosProfile")
            obj.dds_qos_profile = dds_qos_profile_value

        # Parse first_timeout
        child = ARObject._find_child_element(element, "FIRST-TIMEOUT")
        if child is not None:
            first_timeout_value = child.text
            obj.first_timeout = first_timeout_value

        # Parse handle_invalid_enum
        child = ARObject._find_child_element(element, "HANDLE-INVALID-ENUM")
        if child is not None:
            handle_invalid_enum_value = child.text
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
