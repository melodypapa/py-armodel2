"""CanGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 864)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_CAN.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR CanGlobalTimeDomainProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "fup_data_id_list": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # fupDataIDList
        "ofns_data_id_list": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # ofnsDataIDList
        "ofs_data_id_list": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # ofsDataIDList
        "sync_data_id_list": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # syncDataIDList
    }

    def __init__(self) -> None:
        """Initialize CanGlobalTimeDomainProps."""
        super().__init__()
        self.fup_data_id_list: PositiveInteger = None
        self.ofns_data_id_list: PositiveInteger = None
        self.ofs_data_id_list: PositiveInteger = None
        self.sync_data_id_list: PositiveInteger = None


class CanGlobalTimeDomainPropsBuilder:
    """Builder for CanGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanGlobalTimeDomainProps = CanGlobalTimeDomainProps()

    def build(self) -> CanGlobalTimeDomainProps:
        """Build and return CanGlobalTimeDomainProps object.

        Returns:
            CanGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
