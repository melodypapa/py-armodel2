"""SignalServiceTranslationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 336)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1005)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 730)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
    ConsumedEventGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.event_handler import (
    EventHandler,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)


class SignalServiceTranslationProps(Identifiable):
    """AUTOSAR SignalServiceTranslationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "controls": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ConsumedEventGroup,
        ),  # controls
        "control_pncs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PncMappingIdent,
        ),  # controlPncs
        "control_provideds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EventHandler,
        ),  # controlProvideds
        "service_control": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SignalService),
        ),  # serviceControl
        "signal_service_event_propses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SignalService),
        ),  # signalServiceEventPropses
    }

    def __init__(self) -> None:
        """Initialize SignalServiceTranslationProps."""
        super().__init__()
        self.controls: list[ConsumedEventGroup] = []
        self.control_pncs: list[PncMappingIdent] = []
        self.control_provideds: list[EventHandler] = []
        self.service_control: Optional[Any] = None
        self.signal_service_event_propses: list[Any] = []


class SignalServiceTranslationPropsBuilder:
    """Builder for SignalServiceTranslationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationProps = SignalServiceTranslationProps()

    def build(self) -> SignalServiceTranslationProps:
        """Build and return SignalServiceTranslationProps object.

        Returns:
            SignalServiceTranslationProps instance
        """
        # TODO: Add validation
        return self._obj
