"""TriggerPortAnnotation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerPortAnnotation(GeneralAnnotation):
    """AUTOSAR TriggerPortAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Trigger,
        ),  # trigger
    }

    def __init__(self) -> None:
        """Initialize TriggerPortAnnotation."""
        super().__init__()
        self.trigger: Optional[Trigger] = None


class TriggerPortAnnotationBuilder:
    """Builder for TriggerPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerPortAnnotation = TriggerPortAnnotation()

    def build(self) -> TriggerPortAnnotation:
        """Build and return TriggerPortAnnotation object.

        Returns:
            TriggerPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
