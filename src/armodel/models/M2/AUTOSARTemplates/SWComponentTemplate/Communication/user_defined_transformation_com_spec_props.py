"""UserDefinedTransformationComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedTransformationComSpecProps(TransformationComSpecProps):
    """AUTOSAR UserDefinedTransformationComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationComSpecProps."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedTransformationComSpecProps":
        """Deserialize XML element to UserDefinedTransformationComSpecProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedTransformationComSpecProps object
        """
        # Delegate to parent class to handle inherited attributes
        return super(UserDefinedTransformationComSpecProps, cls).deserialize(element)



class UserDefinedTransformationComSpecPropsBuilder:
    """Builder for UserDefinedTransformationComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationComSpecProps = UserDefinedTransformationComSpecProps()

    def build(self) -> UserDefinedTransformationComSpecProps:
        """Build and return UserDefinedTransformationComSpecProps object.

        Returns:
            UserDefinedTransformationComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
