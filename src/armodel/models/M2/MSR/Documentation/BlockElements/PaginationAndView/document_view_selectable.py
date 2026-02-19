"""DocumentViewSelectable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 340)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_PaginationAndView.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameTokens,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ViewTokens,
)
from abc import ABC, abstractmethod


class DocumentViewSelectable(ARObject, ABC):
    """AUTOSAR DocumentViewSelectable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    si: NameTokens
    view: Optional[ViewTokens]
    def __init__(self) -> None:
        """Initialize DocumentViewSelectable."""
        super().__init__()
        self.si: NameTokens = None
        self.view: Optional[ViewTokens] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentViewSelectable":
        """Deserialize XML element to DocumentViewSelectable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentViewSelectable object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse si
        child = ARObject._find_child_element(element, "SI")
        if child is not None:
            si_value = child.text
            obj.si = si_value

        # Parse view
        child = ARObject._find_child_element(element, "VIEW")
        if child is not None:
            view_value = child.text
            obj.view = view_value

        return obj



class DocumentViewSelectableBuilder:
    """Builder for DocumentViewSelectable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentViewSelectable = DocumentViewSelectable()

    def build(self) -> DocumentViewSelectable:
        """Build and return DocumentViewSelectable object.

        Returns:
            DocumentViewSelectable instance
        """
        # TODO: Add validation
        return self._obj
