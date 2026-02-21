"""BswSchedulableEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 75)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 978)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswSchedulableEntity(BswModuleEntity):
    """AUTOSAR BswSchedulableEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BswSchedulableEntity."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize BswSchedulableEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswSchedulableEntity, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "BswSchedulableEntity":
        """Deserialize XML element to BswSchedulableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswSchedulableEntity object
        """
        # Delegate to parent class to handle inherited attributes
        return super(BswSchedulableEntity, cls).deserialize(element)



class BswSchedulableEntityBuilder:
    """Builder for BswSchedulableEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswSchedulableEntity = BswSchedulableEntity()

    def build(self) -> BswSchedulableEntity:
        """Build and return BswSchedulableEntity object.

        Returns:
            BswSchedulableEntity instance
        """
        # TODO: Add validation
        return self._obj
