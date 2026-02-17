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
