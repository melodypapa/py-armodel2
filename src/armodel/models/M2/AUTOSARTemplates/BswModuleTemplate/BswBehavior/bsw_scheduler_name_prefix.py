"""BswSchedulerNamePrefix AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 86)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswSchedulerNamePrefix(ImplementationProps):
    """AUTOSAR BswSchedulerNamePrefix."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BswSchedulerNamePrefix."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize BswSchedulerNamePrefix to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswSchedulerNamePrefix, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswSchedulerNamePrefix":
        """Deserialize XML element to BswSchedulerNamePrefix object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswSchedulerNamePrefix object
        """
        # Delegate to parent class to handle inherited attributes
        return super(BswSchedulerNamePrefix, cls).deserialize(element)



class BswSchedulerNamePrefixBuilder:
    """Builder for BswSchedulerNamePrefix."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswSchedulerNamePrefix = BswSchedulerNamePrefix()

    def build(self) -> BswSchedulerNamePrefix:
        """Build and return BswSchedulerNamePrefix object.

        Returns:
            BswSchedulerNamePrefix instance
        """
        # TODO: Add validation
        return self._obj
