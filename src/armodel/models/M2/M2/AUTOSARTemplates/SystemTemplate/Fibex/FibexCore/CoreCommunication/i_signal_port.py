"""ISignalPort AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_filter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataFilter,
        ),  # dataFilter
        "dds_qos_profile": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsCpQosProfile,
        ),  # ddsQosProfile
        "first_timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # firstTimeout
        "handle_invalid_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HandleInvalidEnum,
        ),  # handleInvalidEnum
        "timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeout
    }

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
