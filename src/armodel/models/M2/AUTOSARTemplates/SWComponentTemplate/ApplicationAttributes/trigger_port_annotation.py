"""TriggerPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerPortAnnotation(GeneralAnnotation):
    """AUTOSAR TriggerPortAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TriggerPortAnnotation."""
        super().__init__()
        self.trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerPortAnnotation":
        """Deserialize XML element to TriggerPortAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TriggerPortAnnotation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.trigger_ref = trigger_ref_value

        return obj



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
