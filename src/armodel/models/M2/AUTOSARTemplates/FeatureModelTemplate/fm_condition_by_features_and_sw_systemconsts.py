"""FMConditionByFeaturesAndSwSystemconsts AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class FMConditionByFeaturesAndSwSystemconsts(ARObject):
    """AUTOSAR FMConditionByFeaturesAndSwSystemconsts."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize FMConditionByFeaturesAndSwSystemconsts."""
        super().__init__()


class FMConditionByFeaturesAndSwSystemconstsBuilder:
    """Builder for FMConditionByFeaturesAndSwSystemconsts."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMConditionByFeaturesAndSwSystemconsts = FMConditionByFeaturesAndSwSystemconsts()

    def build(self) -> FMConditionByFeaturesAndSwSystemconsts:
        """Build and return FMConditionByFeaturesAndSwSystemconsts object.

        Returns:
            FMConditionByFeaturesAndSwSystemconsts instance
        """
        # TODO: Add validation
        return self._obj
