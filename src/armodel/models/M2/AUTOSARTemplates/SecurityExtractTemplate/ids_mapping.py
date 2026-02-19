"""IdsMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class IdsMapping(IdsCommonElement, ABC):
    """AUTOSAR IdsMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize IdsMapping."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsMapping":
        """Deserialize XML element to IdsMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsMapping object
        """
        # Delegate to parent class to handle inherited attributes
        return super(IdsMapping, cls).deserialize(element)



class IdsMappingBuilder:
    """Builder for IdsMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsMapping = IdsMapping()

    def build(self) -> IdsMapping:
        """Build and return IdsMapping object.

        Returns:
            IdsMapping instance
        """
        # TODO: Add validation
        return self._obj
