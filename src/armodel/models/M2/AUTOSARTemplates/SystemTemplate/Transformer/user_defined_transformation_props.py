"""UserDefinedTransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 829)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedTransformationProps(TransformationProps):
    """AUTOSAR UserDefinedTransformationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationProps."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedTransformationProps":
        """Deserialize XML element to UserDefinedTransformationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedTransformationProps object
        """
        # Delegate to parent class to handle inherited attributes
        return super(UserDefinedTransformationProps, cls).deserialize(element)



class UserDefinedTransformationPropsBuilder:
    """Builder for UserDefinedTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationProps = UserDefinedTransformationProps()

    def build(self) -> UserDefinedTransformationProps:
        """Build and return UserDefinedTransformationProps object.

        Returns:
            UserDefinedTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
