"""SenderAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
    SenderReceiverAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SenderAnnotation(SenderReceiverAnnotation):
    """AUTOSAR SenderAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SenderAnnotation."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderAnnotation":
        """Deserialize XML element to SenderAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderAnnotation object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SenderAnnotation, cls).deserialize(element)



class SenderAnnotationBuilder:
    """Builder for SenderAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderAnnotation = SenderAnnotation()

    def build(self) -> SenderAnnotation:
        """Build and return SenderAnnotation object.

        Returns:
            SenderAnnotation instance
        """
        # TODO: Add validation
        return self._obj
