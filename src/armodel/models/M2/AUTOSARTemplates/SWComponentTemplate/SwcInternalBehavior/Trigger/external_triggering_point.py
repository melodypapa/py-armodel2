"""ExternalTriggeringPoint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class ExternalTriggeringPoint(ARObject):
    """AUTOSAR ExternalTriggeringPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ident": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExternalTriggeringPoint,
        ),  # ident
        "trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Trigger,
        ),  # trigger
    }

    def __init__(self) -> None:
        """Initialize ExternalTriggeringPoint."""
        super().__init__()
        self.ident: Optional[ExternalTriggeringPoint] = None
        self.trigger: Optional[Trigger] = None


class ExternalTriggeringPointBuilder:
    """Builder for ExternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExternalTriggeringPoint = ExternalTriggeringPoint()

    def build(self) -> ExternalTriggeringPoint:
        """Build and return ExternalTriggeringPoint object.

        Returns:
            ExternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
