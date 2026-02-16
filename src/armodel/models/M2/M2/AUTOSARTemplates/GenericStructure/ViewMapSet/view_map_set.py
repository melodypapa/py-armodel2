"""ViewMapSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet.view_map import (
    ViewMap,
)


class ViewMapSet(ARElement):
    """AUTOSAR ViewMapSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "view_maps": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ViewMap,
        ),  # viewMaps
    }

    def __init__(self) -> None:
        """Initialize ViewMapSet."""
        super().__init__()
        self.view_maps: list[ViewMap] = []


class ViewMapSetBuilder:
    """Builder for ViewMapSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ViewMapSet = ViewMapSet()

    def build(self) -> ViewMapSet:
        """Build and return ViewMapSet object.

        Returns:
            ViewMapSet instance
        """
        # TODO: Add validation
        return self._obj
