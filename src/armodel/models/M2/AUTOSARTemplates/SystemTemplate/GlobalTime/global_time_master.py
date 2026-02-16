"""GlobalTimeMaster AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)


class GlobalTimeMaster(Identifiable):
    """AUTOSAR GlobalTimeMaster."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "communication_connector": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CommunicationConnector,
        ),  # communicationConnector
        "icv_secured": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=GlobalTimeIcvSupportEnum,
        ),  # icvSecured
        "immediate": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # immediate
        "is_system_wide": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isSystemWide
        "sync_period": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # syncPeriod
    }

    def __init__(self) -> None:
        """Initialize GlobalTimeMaster."""
        super().__init__()
        self.communication_connector: Optional[CommunicationConnector] = None
        self.icv_secured: Optional[GlobalTimeIcvSupportEnum] = None
        self.immediate: Optional[TimeValue] = None
        self.is_system_wide: Optional[Boolean] = None
        self.sync_period: Optional[TimeValue] = None


class GlobalTimeMasterBuilder:
    """Builder for GlobalTimeMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeMaster = GlobalTimeMaster()

    def build(self) -> GlobalTimeMaster:
        """Build and return GlobalTimeMaster object.

        Returns:
            GlobalTimeMaster instance
        """
        # TODO: Add validation
        return self._obj
